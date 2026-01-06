import json
import os

tasks = []

def load_tasks(dir_path="./CLI Todo app/", filename="tasks.json"):
    global tasks
    full_path = os.path.join(dir_path, filename)
    try:
        with open(full_path, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


def save_tasks(dir_path="./CLI Todo app/", filename="tasks.json"):
    full_path = os.path.join(dir_path, filename)
    with open(full_path, "w") as f:
        json.dump(tasks, f)

def add_task(task):
    tasks.append({"task": task, "done": False})

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "done" if task["done"] else "not done"
            print(f"{i+1}. {task['task']} [{status}]")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def menu():
    load_tasks()

    while True:
        print("\n--- To-Do Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            i = int(input("Enter task number to mark done: ")) - 1
            mark_done(i)
        elif choice == "4":
            view_tasks()
            i = int(input("Enter task number to delete: ")) - 1
            delete_task(i)
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# Start the app
menu()
