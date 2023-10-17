# Import necessary libraries
import os

# Constants
TASKS_FILE = "tasks.txt"

# Function to read tasks from the file
def read_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
    return tasks

# Function to create a new task
def create_task(task):
    with open(TASKS_FILE, "a") as file:
        file.write(task + "\n")

# Function to read tasks
def list_tasks():
    tasks = read_tasks()
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")
    else:
        print("Your to-do list is empty.")

# Function to update a task
def update_task(task_index, new_task):
    tasks = read_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index] = new_task + "\n"
        with open(TASKS_FILE, "w") as file:
            file.writelines(tasks)
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    tasks = read_tasks()
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        with open(TASKS_FILE, "w") as file:
            file.writelines(tasks)
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nOptions:")
    print("1. List tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        list_tasks()
    elif choice == "2":
        new_task = input("Enter the task: ")
        create_task(new_task)
    elif choice == "3":
        list_tasks()
        task_index = int(input("Enter the task index to update: ")) - 1
        new_task = input("Enter the new task: ")
        update_task(task_index, new_task)
    elif choice == "4":
        list_tasks()
        task_index = int(input("Enter the task index to delete: ")) - 1
        delete_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
