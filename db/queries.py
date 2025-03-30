CREATE_TABLE_TASKS = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_text TEXT NOT NULL,  -- здесь task_text вместо task
    completed INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    in_progress INTEGER NOT NULL DEFAULT 0
);
"""

SELECT_TASKS = "SELECT id, task_text, completed, created_at, in_progress FROM tasks"

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

UPDATE_TASK_DONE = "UPDATE tasks SET completed = 1 WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

DELETE_TASK_DONE = "DELETE FROM tasks WHERE completed = 1"

SORT_BY_DATE = 'SEJECT id, task, completed, created_at FROM tasks ORDER BY created_at DESC '

SORT_BY_STATUS = 'SEJECT id, task, completed, created_at FROM tasks ORDER BY completed DESC '

SELECT_completed = 'SELECT id, task, completed FROM tasks WHERE completed = 1'

SELECT_incomplete = 'SELECT id, task, completed FROM tasks WHERE completed = 0'