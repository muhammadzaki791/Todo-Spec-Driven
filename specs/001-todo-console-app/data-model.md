# Data Model: Todo Console Application

## Entity: Todo

### Fields
- **id**: Integer (unique, auto-generated)
  - Required: Yes
  - Validation: Must be unique within the application session
  - Purpose: Primary identifier for the todo item

- **title**: String
  - Required: Yes
  - Validation: Must not be empty or whitespace only
  - Maximum length: 200 characters
  - Purpose: Descriptive name of the task

- **description**: String (optional)
  - Required: No
  - Validation: Can be empty or null
  - Maximum length: 1000 characters
  - Purpose: Additional details about the task

- **completed**: Boolean
  - Required: Yes
  - Default value: False
  - Validation: Must be true or false
  - Purpose: Indicates completion status of the task

### State Transitions
- **Incomplete → Complete**: When user marks task as complete
- **Complete → Incomplete**: When user marks task as incomplete

### Validation Rules
1. Title must be provided and not empty
2. ID must be unique within the current session
3. Completed status must be a boolean value
4. Description is optional but if provided, must be a valid string

## Entity: TodoList

### Fields
- **todos**: Dictionary (key: id, value: Todo object)
  - Purpose: Collection of all todo items in the application
  - Access pattern: O(1) lookup by ID

### Relationships
- TodoList contains multiple Todo entities
- Each Todo has a unique ID within the TodoList