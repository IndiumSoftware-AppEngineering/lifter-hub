import sqlite3
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, db_type="sqlite"):
        self.db_type = db_type
        self.connection = None

    def connect(self):
        """Connects to the chosen database (PostgreSQL or SQLite)."""
        if self.db_type == "postgres":
            self.connection = psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT", "5432"),
            )
        else:
            self.connection = sqlite3.connect(os.getenv("SQLITE_DB_PATH", "prompts.db"))
        return self.connection

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()

    def create_table(self):
        """Creates the prompts table if it does not exist."""
        conn = self.connect()
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS prompts (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            content TEXT NOT NULL
        );
        """ if self.db_type == "postgres" else """
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            content TEXT NOT NULL
        );
        """
        
        cursor.execute(create_table_query)
        conn.commit()
        self.close()
