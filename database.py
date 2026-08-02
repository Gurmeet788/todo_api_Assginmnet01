import sqlite3


conn = sqlite3.Connection("tasks.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL
)
""")
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            "INSERT INTO tasks(title, completed) VALUES (?, ?)",
            [
                ("Learn Flask", False),
                ("Learn SQL", True),
                ("Learn Python", True)
            ]
    )
        conn.commit()    