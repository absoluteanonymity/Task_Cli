import json
import datetime
import os
import re





# Json Format for tasks:

# task = {
#     "id": 1,
#     "description": "Task description",
#     "status": "pending",  # pending, in_progress, completed
#     "created_at": "2024-06-01T12:00:00Z",
#     "updated_at": "2024-06-01T12:00:00Z"
# }

#json.dump(data, f, indent=4) Format to write json data to file with indentation for readability

# import json       Loading JSON data from a file

# with open("data.json", "r") as f:
#     data = json.load(f)

# print(data["name"])

def add_task():

    FILE_NAME = "tasks.json"

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

    with open("tasks.json", "r") as f:
        data = json.load(f)
        id = len(data) + 1
    description = input("Enter the task description: ")
    status = input("Enter the task status (pending, in_progress, completed): ")
    created_at = datetime.datetime.now().isoformat()

    task = {
        "id": id,
        "description": description,
        "status": status,
        "created_at": created_at,
        "updated_at": created_at
    }
    with open("tasks.json", "r") as f:
        data = json.load(f)
    
    data.append(task)

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Task '{description}' added successfully with ID {id}.")

def update_task():
    with open("tasks.json", "r") as f:
        data = json.load(f)
    task_id = int(input("Enter the task ID to update: "))
    for task in data:
        if task["id"] == task_id:
            new_description = input("Enter the new description (leave blank to keep current): ")
            new_status = input("Enter the new status (pending, in_progress, completed) (leave blank to keep current): ")
            if new_description:
                task["description"] = new_description
            if new_status:
                task["status"] = new_status
            task["updated_at"] = datetime.datetime.now().isoformat()
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Task ID {task_id} updated successfully.")
            return

def delete_task():
    with open("tasks.json", "r") as f:
        data = json.load(f)
    task_id = int(input("Enter the task ID to delete: "))
    for task in data:
        if task["id"] == task_id:
            data.remove(task)
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Task ID {task_id} deleted successfully.")
            return
    print(f"Task ID {task_id} not found.")

def list_tasks():
    with open("tasks.json", "r") as f:
        data = json.load(f)
    for task in data:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

def list_completed():
    with open("tasks.json", "r") as f:
        data = json.load(f)
        for task in data:
            if task["status"] == "completed":
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")    
                

def list_pending():
    with open("tasks.json", "r") as f:
        data = json.load(f)
        for task in data:
            if task["status"] == "pending":
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")
def list_in_progress():
    with open("tasks.json", "r") as f:
        data = json.load(f)
        for task in data:
            if task["status"] == "in_progress":
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

# Basic Logic for Task Management

program = True

while program:
    print("Cli Task Manager")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. List All Tasks")
    print("5. List Completed Tasks")
    print("6. List All Pending Tasks")
    print("7. List All In Progress Tasks")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        list_completed()
    elif choice == "6":
        list_pending()
    elif choice == "7":
        list_in_progress()
    elif choice == "8":
        program = False
    else:
        print("Invalid choice. Please try again.")
