import sqlite3
import psycopg2
import os

DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # Can be 'sqlite' or 'postgres'

def get_connection():
    if DB_TYPE == "sqlite":
        conn = sqlite3.connect(os.getenv("SQLITE_DB_PATH", "prompts.db"))
    else:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT", "5432"),
        )
    return conn
