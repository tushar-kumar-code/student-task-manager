import sqlite3


def get_connection():
    return sqlite3.connect("database.db")


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            task TEXT NOT NULL,

            priority TEXT DEFAULT 'Medium',

            due_date TEXT,

            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


def add_task(task, priority, due_date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(task, priority, due_date)
        VALUES(?,?,?)
        """,
        (task, priority, due_date)
    )

    conn.commit()
    conn.close()


def get_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def get_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    )

    task = cursor.fetchone()

    conn.close()

    return task


def update_task(task_id, task, priority, due_date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET
            task=?,
            priority=?,
            due_date=?
        WHERE id=?
        """,
        (task, priority, due_date, task_id)
    )

    conn.commit()
    conn.close()


def delete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()


def toggle_status(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT status FROM tasks WHERE id=?",
        (task_id,)
    )

    result = cursor.fetchone()

    if result is None:
        conn.close()
        return

    status = result[0]

    if status == "Pending":
        new_status = "Completed"
    else:
        new_status = "Pending"

    cursor.execute(
        """
        UPDATE tasks
        SET status=?
        WHERE id=?
        """,
        (new_status, task_id)
    )

    conn.commit()
    conn.close()


def get_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Completed'"
    )
    completed = cursor.fetchone()[0]

    pending = total - completed

    conn.close()

    return total, completed, pending