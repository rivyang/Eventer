from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

app = Flask(__name__)

DATABASE_PATH = os.environ.get('DATABASE_PATH', 'community_events.db')

def establish_db_connection():
    return sqlite3.connect(DATABASE_PATH)

def query_db(query, args=(), one=False, commit=False):
    with establish_db_connection() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        if commit:
            conn.commit()
        return (rv[0] if rv else None) if one else rv

@app.route('/events', methods=['POST'])
def create_event_entry():
    event_details = request.json
    query_db('INSERT INTO events (name, description, date, time) VALUES (?, ?, ?, ?)',
             (event_details['name'], event_details['description'], event_details['date'], event_details['time']), commit=True)
    return jsonify({'message': 'Event created successfully'}), 201

@app.route('/events', methods=['GET'])
def fetch_all_events():
    events = query_db('SELECT * FROM events')
    return jsonify([dict(event) for event in events])

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event_details(event_id):
    update_data = request.json
    query_db('UPDATE events SET name = ?, description = ?, date = ?, time = ? WHERE id = ?',
             (update_data['name'], update_data['description'], update_in['date'], update_data['time'], event_id), commit=True)
    return jsonify({'message': 'Event updated successfully'})

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_specific_event(event_id):
    query_db('DELETE FROM events WHERE id = ?', (event_id,), commit=True)
    return jsonify({'message': 'Event deleted successfully'})

@app.route('/register', methods=['POST'])
def register_participant_for_event():
    registration_details = request.json
    query_db('INSERT INTO registrations (user_id, event_id) VALUES (?, ?)',
             (registration_details['user_id'], registration_details['event_id']), commit=True)
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/register/<int:registration_id>', methods=['DELETE'])
def delete_event_registration(registration_id):
    query_db('DELETE FROM registrations WHERE id = ?', (registration_id,), commit=True)
    return jsonify({'message': 'Registration deleted successfully'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_info(user_id):
    user_update_data = request.json
    query_db('UPDATE users SET name = ?, email = ? WHERE id = ?',
             (user_update_data['name'], user_update_data['email'], user_id), commit=True)
    return jsonify({'message': 'User info updated successfully'})

@app.route('/users', methods=['GET'])
def fetch_all_users():
    users = query_db('SELECT * FROM users')
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(debug=True)