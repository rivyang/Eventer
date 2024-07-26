from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    events = db.relationship('Event', secondary='registration', backref=db.backref('attendees', lazy=True))

    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        self._commit_to_db(self)

    def delete(self):
        self._delete_from_db(self)

    @staticmethod
    def _commit_to_db(instance):
        try:
            db.session.add(instance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Failed to save: {e}")

    @staticmethod
    def _delete_from_db(instance):
        try:
            db.session.delete(instance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Failed to delete: {e}")

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Event {self.title}>'

    def save(self):
        self._commit_to_db(self)

    def delete(self):
        self._delete_from_db(self)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    registration_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Registration User: {self.user_id}, Event: {self.event_id}>'

    def save(self):
        self._commit_to_db(self)

    def delete(self):
        self._delete_from_db(self)

for model in [Event, Registration]:
    model._commit_to_db = User._commit_to_db
    model._delete_from_db = User._delete_from_db

if __name__ == '__main__':
    db.create_github.com