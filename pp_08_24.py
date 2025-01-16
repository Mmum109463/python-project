# -*- coding: utf-8 -*-
"""PP-08-24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LXfvOXa3O1cLCq4Kk-yhEoVRqjRX0UXY
"""

#To-Do List with Task Prioritization

import json

TASKS_FILE = "tasks.json"
[
    {
        "description": "Complete Python project",
        "priority": "High",
        "completed": False
    },
    {
        "description": "Buy groceries",
        "priority": "Medium",
        "completed": False
    },
    {
        "description": "Read a book",
        "priority": "Low",
        "completed": True
    }
]
TASKS_FILE = "tasks.json"  # Changed to a filename
[
    {
        "description": "Complete Python project",
        "priority": "High",
        "completed": False  # Changed to False
    },
    {
        "description": "Buy groceries",
        "priority": "Medium",
        "completed": False  # Changed to False
    },
    {
        "description": "Read a book",
        "priority": "Low",
        "completed": True  # Changed to True
    }
]
# Load tasks from the JSON file
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(description, priority):
    tasks = load_tasks()
    task = {
        'description': description,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added with {priority} priority.")

# Mark a task as complete
def complete_task(index):
    tasks = load_tasks()
    if index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index]['description']}' marked as completed.")
    else:
        print("Invalid task index.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if index < len(tasks):
        task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{task['description']}' deleted.")
    else:
        print("Invalid task index.")

# View all tasks, sorted by priority
def view_tasks():
    tasks = load_tasks()
    sorted_tasks = sorted(tasks, key=lambda x: x['priority'], reverse=True)

    if tasks:
        print("Your tasks:")
        for i, task in enumerate(sorted_tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['description']} [{task['priority']}] - {status}")
    else:
        print("No tasks found.")

# Main menu
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (High, Medium, Low): ").capitalize()
            if priority not in ['High', 'Medium', 'Low']:
                print("Invalid priority. Please choose 'High', 'Medium', or 'Low'.")
            else:
                add_task(description, priority)
        elif choice == "2":
            view_tasks()
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

[
    {
        "description": "Complete Python project",
        "priority": "High",
        "completed": False
    },
    {
        "description": "Buy groceries",
        "priority": "Medium",
        "completed": False
    },
    {
        "description": "Read a book",
        "priority": "Low",
        "completed": True
    }
]