from  . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True)  # Primary Key
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    job_preferences = db.Column(db.Text)  # JSON or text field for preferences
    date_added = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    # Relationships
    profile = db.relationship('Profile', back_populates='user', uselist=False)  # One-to-One
    recommendations = db.relationship('Recommendations', back_populates='user', lazy=True)  # One-to-Many

    # Override get_id to use 'userid' instead of 'id'
    def get_id(self):
        return str(self.userid)
        
class Profile(db.Model):
    __tablename__ = 'profile'
    profileid = db.Column(db.Integer, primary_key=True)  # Primary Key
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False)  # Foreign Key
    resume = db.Column(db.Text)
    skills = db.Column(db.Text)
    experience = db.Column(db.Text)

    # Relationship back to the User
    user = db.relationship('User', back_populates='profile')  # One-to-One

class Recommendations(db.Model):
    __tablename__ = 'recommendations'
    recommendationid = db.Column(db.Integer, primary_key=True)  # Primary Key
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False)  # Foreign Key to User
    jobid = db.Column(db.Integer, db.ForeignKey('jobs.jobid'), nullable=False)  # Foreign Key to Job
    recommended_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='recommendations')  # Many-to-One with User
    job = db.relationship('Jobs', back_populates='recommendations')  # Many-to-One with Jobs

class Jobs(db.Model):
    __tablename__ = 'jobs'
    jobid = db.Column(db.Integer, primary_key=True)  # Primary Key
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)

    # Relationship to Recommendations
    recommendations = db.relationship('Recommendations', back_populates='job')  # Many-to-One