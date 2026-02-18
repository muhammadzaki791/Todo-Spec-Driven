# Todo Console Application

A simple in-memory todo application built with Python.

## Features
- Add todo items with title and optional description
- View all todo items with their completion status
- Update existing todo items
- Delete todo items
- Mark todo items as complete or incomplete

## Setup
1. Ensure Python 3.13+ is installed
2. Install dependencies using UV: `uv sync`
3. Run the application: `python src/cli/main.py`

## Usage
Run the application and use the following commands:
- `add "title" "optional description"` - Add a new todo
- `view` - View all todos
- `update <id> "new title" "optional new description"` - Update a todo
- `delete <id>` - Delete a todo
- `complete <id>` - Mark a todo as complete
- `incomplete <id>` - Mark a todo as incomplete
- `exit` - Exit the application