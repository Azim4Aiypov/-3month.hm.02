CREATE_TABLE_TASKS = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completd INTEGER DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

SELECT_TASKS = "SELECT id, task, created_at, completed FROM tasks"

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

UPDATE_TASK_DONE = "UPDATE FROM tasks WHERE completed =1"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

DELETE_TASK_DONE = "DELETE FROM tasks WHERE completed = 1"

SORT_BY_DATE = "SELECT id, task, created_at, completed FROM tasks ORDER_BY created_at DESC"

SORT_BY_STATUS = "SELECT id, task, created_at, completed FROM tasks ORDER_BY completed DESC"

SELECT_completed = "SELECT id, task, completed FROM tasks WHERE completed = 1"

SELECT_incomplete = "SELECT id, task, completed FROM tasks WHERE completed = 0"
