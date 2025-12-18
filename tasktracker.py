import sys
import json
from datetime import datetime

FILENAME = "tasks.json"


def load_data():
    try:
        with open(FILENAME, "r") as f:
            text = f.read().strip()
            if text == "":
                data = {"nextId": 1, "tasks": []}
                save_data(data)
                return data
            return json.loads(text)
    except FileNotFoundError:
        data = {"nextId": 1, "tasks": []}
        save_data(data)
        return data
    

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)


def add_task(description):
    data = load_data()

    task = {
        "id": data["nextId"],
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    data["tasks"].append(task)
    data["nextId"] += 1

    save_data(data)
    print(f"Task added (ID: {task['id']})")


def list_tasks():
    data = load_data()

    for task in data["tasks"]:
        print(f"{task['id']} [{task['status']}] {task['description']}")


def mark_done(task_id):
    data = load_data()

    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_data(data)
            print("Task marked as done")
            return

    print("Task not found")


def main():
    if len(sys.argv) < 2:
        print("Usage: python tasktracker.py <add|list|mark-done> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python tasktracker.py add <description>")
            return
        description = sys.argv[2]
        add_task(description)

    elif command == "list":
        list_tasks()

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python tasktracker.py mark-done <task-id>")
            return
        task_id = int(sys.argv[2])
        mark_done(task_id)

    else:
        print("Unknown command")


main()
