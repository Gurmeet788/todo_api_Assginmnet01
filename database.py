import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():

    return psycopg.connect(
        os.getenv("DATABASE_URL")
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT False
        )
        """)
        cursor.execute("SELECT COUNT(*) FROM tasks")
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.executemany(
                "INSERT INTO tasks(title, completed) VALUES (%s, %s)",
                [
                    ("Learn Flask", False),
                    ("Learn SQL", True),
                    ("Learn Python", True)
                ]
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()    