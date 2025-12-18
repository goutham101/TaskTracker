# TaskTracker(Python)
A simple command-line application to track tasks using Python and a local JSON file.

---

## Requirements

- Python 3
- Terminal / Command Prompt

No external libraries required.

---

## Setup

1. Clone or download this repository
2. Ensure the project directory contains:
   - `tasktracker.py`
   - `tasks.json`

If `tasks.json` does not exist or is empty, the program will create and initialize it automatically.

---

## How to Use

Run all commands from the project directory.

### Add a Task
Command: python tasktracker.py add "Buy groceries"
Adds a new task with a unique ID and a default status of todo.

### List All Tasks
Command: python tasktracker.py list
Displays all tasks with their ID, status, and description.

### Mark a Task as Done
Command: python tasktracker.py mark-done 1
Marks the task with ID 1 as completed.

---


### Task Format

Each task is stored with the following fields:
id — unique task identifier
description — task description
status — todo or done
createdAt — timestamp when the task was created
updatedAt — timestamp of the last update
All task data is saved locally in tasks.json.

---


### Notes

Task descriptions containing spaces must be wrapped in quotes
Commands must be run from the directory containing tasktracker.py
Task data persists between executions
