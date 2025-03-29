import sqlite3
from config import DB_PATH
from db import queries


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASKS)
    conn.commit()
    conn.close()


def get_tasks(filter_type="all"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # cursor.execute(queries.SELECT_TASKS)

    if filter_type == 'completed':
        cursor.execute(queries.SELECT_completed)
    elif filter_type == "incomplete":
        cursor.execute(queries.SELECT_incomplete)
    else:
        cursor.execute(queries.SELECT_TASKS)

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task_db(task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task,))
    task_id = cursor.lastrowid
    cursor.execute("SELECT created_at FROM tasks WHERE id = ?", (task_id,))
    created_at = cursor()[0]
    conn.commit()
    conn.close()
    return task_id ,task , created_at


def update_task_db(task_id, new_task=None, completed=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # cursor.execute(queries.UPDATE_TASK, (new_task, task_id))

    if new_task is not None:
        cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    if completed is not None:
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))

    conn.commit()
    conn.close()

def delete_task_db(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()

def delete_done():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK_DONE, )
    conn.commit()
    conn.close()

def done_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK_DONE, (task_id,))
    conn.commit()
    conn.close()
    


def sort_task_date():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.SORT_BY_DATE)
    task = cursor.fetchall()
    conn.commit()
    conn.close()
    return task

def sort_task_status():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.SORT_BY_STATUS,)
    task = cursor.fetchall()
    conn.commit()
    conn.close()
    return task
# pip install flet[all]