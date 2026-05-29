import sqlite3

def upgrade():
    conn = sqlite3.connect('bmi_tracker.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN current_streak INTEGER DEFAULT 0")
        cursor.execute("ALTER TABLE users ADD COLUMN last_log_date DATETIME")
    except sqlite3.OperationalError as e:
        print("Columns might already exist:", e)
        
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS progress_photos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                filename VARCHAR(256) NOT NULL,
                uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
    except sqlite3.OperationalError as e:
        print("Could not create photos table:", e)
        
    conn.commit()
    conn.close()
    print("Migration successful.")

if __name__ == "__main__":
    upgrade()
