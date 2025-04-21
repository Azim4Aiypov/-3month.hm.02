# db/queries.py

CREATE_TABLE_TASKS = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed INTEGER DEFAULT 0
)
"""

SELECT_TASKS = "SELECT id, task, created_at, completed FROM tasks"

INSERT_TASK = "INSERT INTO tasks (task, created_at, completed) VALUES (?, CURRENT_TIMESTAMP, 0)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

UPDATE_COMPLETED = "UPDATE tasks SET completed = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"
