from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

app = Flask(__name__)

DATABASE_PATH = os.environ.get('DATABASE_PATH', 'community_events.db')

def establish_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/events', methods=['POST'])
def create_event_entry():
    event_details = request.json
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('INSERT INTO events (name, description, date, time) VALUES (?, ?, ?, ?)',
                      (event_details['name'], event_details['description'], event_details['date'], event_details['time']))
    db_connection.commit()
    db_connection.close()
    return jsonify({'message': 'Event created successfully'}), 201

@app.route('/events', methods=['GET'])
def fetch_all_events():
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM events')
    events = db_cursor.fetchall()
    db_connection.close()
    return jsonify([dict(event) for event in events])

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event_details(event_id):
    update_data = request.json
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('UPDATE events SET name = ?, description = ?, date = ?, time = ? WHERE id = ?',
                      (update_data['name'], update_data['description'], update_data['date'], update_data['time'], event_id))
    db_connection.commit()
    db_connection.close()
    return jsonify({'message': 'Event updated successfully'})

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_specific_event(event_id):
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
    db_connection.commit()
    db_connection.close()
    return jsonify({'message': 'Event deleted successfully'})

@app.route('/register', methods=['POST'])
def register_participant_for_event():
    registration_details = request.json
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('INSERT INTO registrations (user_id, event_id) VALUES (?, ?)',
                      (registration_details['user_id'], registration_details['event_id']))
    db_connection.commit()
    db_connection.close()
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/register/<int:registration_id>', methods=['DELETE'])
def delete_event_registration(registration_id):
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('DELETE FROM registrations WHERE id = ?', (registration_id,))
    db_connection.commit()
    db_connection.close()
    return jsonify({'message': 'Registration deleted successfully'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_info(user_id):
    user_update_data = request.json
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?',
                      (user_update_data['name'], user_update_data['email'], user_id))
    db_connection.commit()
    db_connection.close()
    return jsonify({'message': 'User info updated successfully'})

@app.route('/users', methods=['GET'])
def fetch_all_users():
    db_connection = establish_db_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM users')
    users = db_cursor.fetchall()
    db_connection.close()
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(debug=True)