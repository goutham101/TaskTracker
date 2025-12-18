# TaskTracker(Python)
Requirements

Python 3 installed

Terminal / Command Prompt

No external libraries required.

Setup

Clone or download this repository

Make sure the project folder contains:

tasktracker.py

tasks.json

If tasks.json does not exist, the program will create it automatically.

How to Use

All commands are run from the terminal in the project directory.

Add a Task
python tasktracker.py add "Buy groceries"


Adds a new task with a unique ID and a default status of todo.

List All Tasks
python tasktracker.py list


Displays all tasks with their ID, status, and description.

Mark a Task as Done
python tasktracker.py mark-done 1


Marks the task with ID 1 as completed.

Task Format

Each task is stored with the following fields:

id – unique task identifier

description – task description

status – todo or done

createdAt – timestamp when the task was created

updatedAt – timestamp of the last update

All data is saved locally in tasks.json.

Notes

Descriptions containing spaces must be wrapped in quotes

Commands must be run from the directory containing tasktracker.py

Task data persists between runs
