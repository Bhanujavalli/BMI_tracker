import sqlite3

def migrate():
    conn = sqlite3.connect('bmi_tracker.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE bmi_records ADD COLUMN foods_to_eat TEXT;")
        print("Added foods_to_eat")
    except Exception as e:
        print(f"foods_to_eat: {e}")
        
    try:
        cursor.execute("ALTER TABLE bmi_records ADD COLUMN foods_to_avoid TEXT;")
        print("Added foods_to_avoid")
    except Exception as e:
        print(f"foods_to_avoid: {e}")
        
    try:
        cursor.execute("ALTER TABLE bmi_records ADD COLUMN daily_tips TEXT;")
        print("Added daily_tips")
    except Exception as e:
        print(f"daily_tips: {e}")
        
    conn.commit()
    conn.close()
    print("Migration complete.")

if __name__ == "__main__":
    migrate()
