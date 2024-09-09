#import sqlite3
#from datetime import datetime
#def connect():
#    conn = sqlite3.connect('todo_list.db')  # Connect to the database (or create it)
#    cursor = conn.cursor()

#    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                      id INTEGER PRIMARY KEY AUTOINCREMENT,
#                      task TEXT NOT NULL,
#                      priority INTEGER,
#                      date_added TEXT,
#                      due_date TEXT,
#                      status TEXT)''')

#    conn.commit()
#    return conn


#def reset_table():
#    conn = connect()
#    cursor = conn.cursor()

#    cursor.execute("DROP TABLE IF EXISTS tasks")  
#    conn.commit()
#    conn.close()

#reset_table()


#from datetime import datetime
#from sqlite3 import connect

#def add_task(task, priority=1, due_date=None):
#    conn = connect()
#    cursor = conn.cursor()

#    date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    status = 'Pending'  # Default task status

#    cursor.execute('''INSERT INTO tasks (task, priority, date_added, due_date, status)
#                      VALUES (?, ?, ?, ?, ?)''', (task, priority, date_added, due_date, status))

#    conn.commit()
#    conn.close()

#    print(f"Task '{task}' added with priority {priority} and due date{due_date}.")


#def view_tasks():
#    conn = connect()
#    cursor = conn.cursor()

#    cursor.execute("SELECT * FROM tasks")
#    tasks = cursor.fetchall()

#    conn.close()

#    if tasks:
#        for task in tasks:
#            print(f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}, Added on: {task[3]}, Due: {task[4]}, Status: {task[5]}")
#    else:
#        print("No tasks found.")

#def mark_task_complete(task_id):
#    conn = connect()
#    cursor = conn.cursor()

#    cursor.execute('''UPDATE tasks
#                      SET status = ?
#                      WHERE id = ?''', ('Completed', task_id))

#    conn.commit()
#    conn.close()

#    print(f"Task ID {task_id} marked as completed.")

#def delete_task(task_id):
#    conn = connect()
#    cursor = conn.cursor()

#    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))

#    conn.commit()
#    conn.close()

#    print(f"Task ID {task_id} deleted.")

#def view_tasks_sorted_by_priority():
#    conn = connect()
#    cursor = conn.cursor()

#    cursor.execute("SELECT * FROM tasks ORDER BY priority ASC")
#    tasks = cursor.fetchall()

#    conn.close()

#    for task in tasks:
#        print(f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}, Added on: {task[3]}, Due: {task[4]}, Status: {task[5]}")

#add_task("Buy groceries", priority=2, due_date="2024-09-07")

#view_tasks()

#mark_task_complete(1)

#delete_task(2)

#view_tasks_sorted_by_priority()


######################################


import sqlite3
from datetime import datetime

def connect():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      task TEXT NOT NULL,
                      priority INTEGER,
                      date_added TEXT,
                      due_date TEXT,
                      status TEXT)''')
    conn.commit()
    return conn

def add_task(task, priority=1, due_date=None):
    conn = connect()
    cursor = conn.cursor()

    date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = 'Pending'

    cursor.execute('''INSERT INTO tasks (task, priority, date_added, due_date, status)
                      VALUES (?, ?, ?, ?, ?)''', (task, priority, date_added, due_date, status))

    conn.commit()
    conn.close()

    print(f"Task '{task}' added.")

def view_tasks():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE status = 'Pending' ORDER BY priority ASC")
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}, Added on: {task[3]}, Due: {task[4]}, Status: {task[5]}")
    else:
        print("No tasks found.")

def mark_task_complete(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''UPDATE tasks SET status = ? WHERE id = ?''', ('Completed', task_id))

    conn.commit()
    conn.close()

    print(f"Task ID {task_id} marked as completed.")

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))

    conn.commit()
    conn.close()

    print(f"Task ID {task_id} deleted.")

def view_tasks_sorted_by_priority():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks ORDER BY priority ASC")
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Priority: {task[2]}, Added on: {task[3]}, Due: {task[4]}, Status: {task[5]}")
    else:
        print("No tasks found.")

add_task("Buy groceries", priority=2, due_date="2025-06-13")
view_tasks()
mark_task_complete(1)
delete_task(2)
view_tasks_sorted_by_priority()
