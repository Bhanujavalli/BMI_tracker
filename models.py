from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    
    # Basic Profile info
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Float, nullable=False) # Height stored uniquely per user to prevent random changes
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    current_streak = db.Column(db.Integer, default=0)
    last_log_date = db.Column(db.DateTime, nullable=True)

    records = db.relationship('BMIRecord', backref='user', lazy=True)
    photos = db.relationship('ProgressPhoto', backref='user', lazy=True)

class ProgressPhoto(db.Model):
    __tablename__ = 'progress_photos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(256), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class BMIRecord(db.Model):
    __tablename__ = 'bmi_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    weight = db.Column(db.Float, nullable=False)  # Current weight recorded
    height_used = db.Column(db.Float, nullable=False) # Saved height at the time
    bmi_value = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    
    # AI recommendations snapshots
    health_risk = db.Column(db.Text, nullable=True)
    diet_recommendation = db.Column(db.Text, nullable=True)
    foods_to_eat = db.Column(db.Text, nullable=True)
    foods_to_avoid = db.Column(db.Text, nullable=True)
    exercise_plan = db.Column(db.Text, nullable=True)
    lifestyle_advice = db.Column(db.Text, nullable=True)
    daily_tips = db.Column(db.Text, nullable=True)
    health_summary = db.Column(db.Text, nullable=True)
    
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
