-- MySQL Schema for AI-Based BMI Health Tracker (as per database requirements)
-- Run this if migrating the backend to MySQL rather than default SQLite.

CREATE DATABASE IF NOT EXISTS bmi_db;
USE bmi_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(256) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    height FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bmi_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    weight FLOAT NOT NULL,
    height_used FLOAT NOT NULL,
    bmi_value FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    health_risk TEXT,
    diet_recommendation TEXT,
    exercise_plan TEXT,
    lifestyle_advice TEXT,
    health_summary TEXT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
