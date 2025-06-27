import sqlite3

DB_PATH = "counters.db"

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