from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'community_events.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO events (name, description, date, time) VALUES (?, ?, ?, ?)',
                   (data['name'], data['description'], data['date'], data['time']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Event created successfully'}), 201

@app.route('/events', methods=['GET'])
def get_events():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events')
    events = cursor.fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in events])

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE events SET name = ?, description = ?, date = ?, time = ? WHERE id = ?',
                   (data['name'], data['description'], data['date'], data['time'], event_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Event updated successfully'})

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Event deleted successfully'})

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO registrations (user_id, event_id) VALUES (?, ?)',
                   (data['user_id'], data['event_id']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/register/<int:registration_id>', methods=['DELETE'])
def delete_registration(registration_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM registrations WHERE id = ?', (registration_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registration deleted successfully'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?',
                   (data['name'], data['email'], user_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User info updated successfully'})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in users])

if __name__ == '__main__':
    app.run(debug=True)