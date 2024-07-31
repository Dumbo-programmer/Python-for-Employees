import requests

def task_management():
    print("Welcome to the Task Management Script!")
    api_url = input("Enter the task management API URL: ")
    api_key = input("Enter your API key: ")
    task_action = input("Do you want to (1) Create or (2) Update a task? ")

    if task_action == "1":
        task_title = input("Enter the task title: ")
        task_description = input("Enter the task description: ")
        response = requests.post(api_url + "/tasks", json={"title": task_title, "description": task_description}, headers={"Authorization": f"Bearer {api_key}"})
        print("Task created:", response.json())

    elif task_action == "2":
        task_id = input("Enter the task ID to update: ")
        new_title = input("Enter the new task title: ")
        new_description = input("Enter the new task description: ")
        response = requests.put(api_url + f"/tasks/{task_id}", json={"title": new_title, "description": new_description}, headers={"Authorization": f"Bearer {api_key}"})
        print("Task updated:", response.json())

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    task_management()
