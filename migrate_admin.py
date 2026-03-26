import sqlite3
from werkzeug.security import generate_password_hash
from datetime import datetime

def migrate():
    conn = sqlite3.connect('bmi_tracker.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT 0;")
        print("Added is_admin to users table")
    except Exception as e:
        print(f"is_admin: {e}")
        
    # Check if admin user exists
    cursor.execute("SELECT id FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        hashed_password = generate_password_hash('admin123', method='scrypt')
        cursor.execute(
            """INSERT INTO users (username, password_hash, age, gender, height, is_admin, created_at) 
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            ('admin', hashed_password, 30, 'other', 170.0, 1, datetime.utcnow())
        )
        print("Seeded 'admin' user successfully.")
    else:
        # Just ensure they are marked as admin
        cursor.execute("UPDATE users SET is_admin = 1 WHERE username = 'admin'")
        print("Admin user already exists, updated is_admin to 1.")
        
    conn.commit()
    conn.close()
    print("Admin migration complete.")

if __name__ == "__main__":
    migrate()
