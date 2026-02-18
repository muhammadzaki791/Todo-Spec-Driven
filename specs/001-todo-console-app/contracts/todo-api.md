# Todo API Contracts

## Core Operations

### Add Todo
- **Command**: `add "title" "description"`
- **Input**: Title (required string), Description (optional string)
- **Output**: Success message with assigned ID
- **Errors**: Invalid input format

### View Todos
- **Command**: `view`
- **Input**: None
- **Output**: List of all todos with ID, title, description, and completion status
- **Errors**: None

### Update Todo
- **Command**: `update <id> "title" "description"`
- **Input**: ID (required integer), Title (required string), Description (optional string)
- **Output**: Success message
- **Errors**: Invalid ID, Invalid input format

### Delete Todo
- **Command**: `delete <id>`
- **Input**: ID (required integer)
- **Output**: Success message
- **Errors**: Invalid ID

### Mark Complete/Incomplete
- **Command**: `complete <id>` or `incomplete <id>`
- **Input**: ID (required integer)
- **Output**: Success message
- **Errors**: Invalid ID