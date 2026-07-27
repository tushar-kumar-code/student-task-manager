import sqlite3


def create_database():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            task TEXT NOT NULL

        )
    """)

    conn.commit()

    conn.close()


def add_task(task):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(task) VALUES(?)",
        (task,)
    )

    conn.commit()

    conn.close()


def get_tasks():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def delete_task(task_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()

    conn.close()