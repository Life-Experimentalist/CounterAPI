import os
import sqlite3

DB_PATH = os.getenv("DB_PATH", "./counters.db")

# Ensure the directory for the DB exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                name TEXT PRIMARY KEY,
                description TEXT,
                count INTEGER DEFAULT 0
            )
        """)

def get_db():
    return sqlite3.connect(DB_PATH)
