import sqlite3
import datetime

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    tags TEXT,
    added_at TEXT NOT NULL,
    completed_at TEXT
)
''')
conn.commit()

def add_task(task_description, task_tags):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tags = ", ".join(task_tags)
    
    cursor.execute('''
        INSERT INTO tasks (description, tags, added_at, completed_at)
        VALUES (?, ?, ?, ?)
    ''', (task_description, tags, timestamp, None))
    
    conn.commit()
    print(f"Task added: {task_description}")

def remove_task(task_id):

    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Removed task with ID {task_id}")
    else:
        print("Invalid task ID")

def view_tasks():
    cursor.execute('SELECT id, description, tags, added_at, completed_at FROM tasks')
    tasks = cursor.fetchall()
    
    if not tasks:
        print("No tasks to display.")
        return

    for task in tasks:
        task_id, description, tags, added_at, completed_at = task
        completion_status = f" (completed at {completed_at})" if completed_at else ""
        print(f"{task_id}: {description} (tags: {tags}, added at {added_at}){completion_status}")

def main():
    while True:
        command = input("Enter command (add/view/remove/quit): ").strip().lower()

        if command == "add":
            description = input("Enter the task description: ")
            tags_input = input("Enter tags separated by commas (leave empty if no tags): ")
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            add_task(description, tags)
        elif command == "view":
            view_tasks()
        elif command.startswith("remove"):
            try:
                task_id = int(command.split()[1])
                remove_task(task_id)
            except (IndexError, ValueError):
                print("Please provide a valid task ID to remove.")
        elif command == "quit":
            break
        else:
            print("Unknown command. Please use 'add', 'view', 'remove', or 'quit'.")



    main()
