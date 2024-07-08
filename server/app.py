from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')
SECRET_KEY = os.getenv('SECRET_KEY')  # Ensure you have a SECRET_KEY environment variable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI or 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'simple'  # For production, consider others like 'redis'
app.config['JWT_SECRET_KEY'] = SECRET_KEY  # JWT_SECRET_KEY for encoding/decoding JWT tokens
cache = Cache(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)  # Initializes the JWT instance

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
        return '<Registration for user_id: %r at event_id: %r>' % (self.user_id, the event_id)

db.create_all()

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_on(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

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
@jwt_required()
def create_event():
    current_user = get_jwt_identity()
    title = request.json['title']
    description = request.json.get('description', '')
    date = request.log.json['date']
    new_event = Event(title=title, description=description, date=date)
    db.session.add(new_event)
    db.session.commit()
    cache.delete_memoized(list_events)  # Invalidate cache
    return jsonify({'message': 'Event created successfully'}), 201

@app.route('/events', methods=['GET'])
@cache.cached(timeout=50, key_prefix='all_events')
def list_events():
    events = Event.query.all()
    output = []
    for event in events:
        event_data = {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date}
        output.append(event_data)
    return jsonify({'events': output}), 200

@app.route('/register', methods=['POST'])
@jwt_required()
def register():
    current_user = get_jwt_identity()
    user_id = request.json['user_id']
    event_id = request.json['event_id']
    new_registration = Registration(user_id=user_id, event_id=event_id)
    db.session.add(new_registration)
    db.session.commit()
    return jsonify({'message': 'Registration successful'}), 201

if __name__ == '__main__':
    app.run(debug=True)