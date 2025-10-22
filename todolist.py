# Simple To-Do List Manager

# Initialize an empty list to store tasks
todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for idx, t in enumerate(todo_list, 1):
            status = "✓ Done" if t["done"] else "✗ Not Done"
            print(f"{idx}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            print(f"Task '{todo_list[task_num - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
