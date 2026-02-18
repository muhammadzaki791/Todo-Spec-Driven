# Quickstart Guide: Todo Console Application

## Setup

1. Ensure Python 3.13+ is installed
2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Running the Application

To run the application:
```bash
python src/cli/main.py
```

## Using the Application

Once the application is running, you can use the following commands:

### Add a new todo
```
add "Title of the task" "Optional description"
```

### View all todos
```
view
```

### Update a todo
```
update <id> "New title" "Optional new description"
```

### Mark a todo as complete/incomplete
```
complete <id>  # Mark as complete
incomplete <id>  # Mark as incomplete
```

### Delete a todo
```
delete <id>
```

### Exit the application
```
exit
```

## Example Usage

```
> add "Buy groceries" "Milk, bread, eggs"
Added todo #1: Buy groceries

> add "Finish report" "Complete the quarterly report"
Added todo #2: Finish report

> view
1. [ ] Buy groceries - Milk, bread, eggs
2. [ ] Finish report - Complete the quarterly report

> complete 1
Todo #1 marked as complete

> view
1. [x] Buy groceries - Milk, bread, eggs
2. [ ] Finish report - Complete the quarterly report

> exit
```