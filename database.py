import os

import psycopg2

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_SCHEMA = os.getenv(
    "DB_SCHEMA", "myschema"
)  # Set your schema name here or via env var


def get_db():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )
    # Set search_path to your schema
    conn.cursor().execute(f"SET search_path TO {DB_SCHEMA};")
    return conn
