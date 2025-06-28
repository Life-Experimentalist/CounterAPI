import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "/data/counters.db")

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
