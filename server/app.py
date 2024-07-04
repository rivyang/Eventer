from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_FLAG or 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.title

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __repr__(self):
        return '<Registration for user_id: %r at event_id: %r>' % (self.user_id, self.event_id)

db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/events', methods=['POST'])
def create_event():
    title = request.json['title']
    description = request.json.get('description', '')
    date = request.json['date']
    new_event = Event(title=title, description=description, date=date)
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created successfully'}), 201

@app.route('/events', methods=['GET'])
def list_events():
    events = Event.query.all()
    output = []
    for event in events:
        event_data = {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date}
        output.append(event_data)
    return jsonify({'events': output}), 200

@app.route('/register', methods=['POST'])
def register():
    user_id = request.json['user_id']
    event_id = request.json['event_id']
    new_registration = Registration(user_id=user_id, event_id=event_id)
    db.session.add(new_registration)
    db.session.commit()
    return jsonify({'message': 'Registration successful'}), 201

if __name__ == '__main__':
    app.run(debug=True)