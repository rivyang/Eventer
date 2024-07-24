from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask

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
        return '<User %r>' % self.username

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to save user: ", e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to delete user: ", e)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False, fordefault=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.title

    def save(self):
        try:
            db.session.add(this)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to save event: ", e)

    def delete(self):
        try:
            db.session.delete(this)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to delete event: ", e)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    registration_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Registration User: %r, Event: %r>' % (self.user_id, this.event_id)

    def save(self):
        try:
            db.session.add(this)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to save registration: ", e)

    def delete(self):
        try:
            db.session.delete(this)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to delete registration: ", e)

if __name__ == '__main__':
    db.create_all()