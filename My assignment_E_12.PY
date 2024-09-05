import datetime

todo_list = []

def add_task(task_description, task_tags):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todo_list.append({
        "description": task_description,
        "tags": task_tags,
        "added_at": timestamp,
        "completed_at": None
    })

def remove_task(index):
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"Removed task: {removed_task['description']}")
    else:
        print("Invalid task number")

def view_tasks():
    if not todo_list:
        print("No tasks to display.")
        return

    for i, item in enumerate(todo_list):
        description = item["description"]
        tags = ", ".join(item["tags"])
        added_at = item["added_at"]
        completed_at = item["completed_at"]
        completion_status = f" (completed at {completed_at})" if completed_at else ""
        print(f"{i + 1}: {description} (tags: {tags}, added at {added_at}){completion_status}")

def main():
    while True:
        command = input("Enter command (add/view/remove/quit): ").strip().lower()

        if command == "add":
            description = input("Enter the task description: ")
            tags_input = input("Enter tags separated by commas (leave empty if no tags): ")
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            add_task(description, tags)
            print(f"Task added: {description}")
        elif command == "view":
            view_tasks()
        elif command.startswith("remove"):
            try:
                index = int(command.split()[1]) - 1
                remove_task(index)
            except (IndexError, ValueError):
                print("Please provide a valid task number to remove.")
        elif command == "quit":
            break
        else:
            print("Unknown command. Please use 'add', 'view', 'remove', or 'quit'.")

if __name__ == "_main_":main()