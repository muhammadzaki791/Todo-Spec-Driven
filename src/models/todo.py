"""
Todo data model with ID, title, description, and completion status.
"""
from typing import Optional


class Todo:
    """
    Represents a todo item with ID, title, description, and completion status.
    """

    def __init__(self, id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Todo object.

        Args:
            id (int): Unique identifier for the todo
            title (str): Title of the todo (required)
            description (str, optional): Description of the todo (optional)
            completed (bool): Completion status of the todo (default: False)
        """
        if not title or not title.strip():
            raise ValueError("Title must be provided and not empty")

        if len(title) > 200:
            raise ValueError("Title must not exceed 200 characters")

        if description and len(description) > 1000:
            raise ValueError("Description must not exceed 1000 characters")

        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else description
        self.completed = completed

    def __str__(self):
        """
        String representation of the Todo object.
        """
        status = "x" if self.completed else " "
        description_str = f" - {self.description}" if self.description else ""
        return f"{self.id}. [{status}] {self.title}{description_str}"

    def __repr__(self):
        """
        Developer-friendly representation of the Todo object.
        """
        return f"Todo(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"


class TodoList:
    """
    Collection of Todo items stored in memory using a dictionary.
    Provides O(1) lookup by ID.
    """

    def __init__(self):
        """
        Initialize an empty TodoList.
        """
        self.todos = {}  # Dictionary with key: id, value: Todo object

    def add_todo(self, todo: Todo) -> bool:
        """
        Add a todo to the collection.

        Args:
            todo (Todo): The Todo object to add

        Returns:
            bool: True if added successfully, False if ID already exists
        """
        if todo.id in self.todos:
            return False
        self.todos[todo.id] = todo
        return True

    def get_todo(self, id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            id (int): The ID of the todo to retrieve

        Returns:
            Todo: The Todo object if found, None otherwise
        """
        return self.todos.get(id)

    def get_all_todos(self) -> list:
        """
        Get all todos in the collection.

        Returns:
            list: List of all Todo objects
        """
        return list(self.todos.values())

    def update_todo(self, id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a todo by its ID.

        Args:
            id (int): The ID of the todo to update
            title (str, optional): New title for the todo
            description (str, optional): New description for the todo

        Returns:
            bool: True if updated successfully, False if todo not found
        """
        if id not in self.todos:
            return False

        todo = self.todos[id]
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title must be provided and not empty")
            if len(title) > 200:
                raise ValueError("Title must not exceed 200 characters")
            todo.title = title.strip()

        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description must not exceed 1000 characters")
            todo.description = description.strip() if description else description

        return True

    def delete_todo(self, id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            id (int): The ID of the todo to delete

        Returns:
            bool: True if deleted successfully, False if todo not found
        """
        if id not in self.todos:
            return False
        del self.todos[id]
        return True

    def mark_complete(self, id: int) -> bool:
        """
        Mark a todo as complete by its ID.

        Args:
            id (int): The ID of the todo to mark as complete

        Returns:
            bool: True if marked successfully, False if todo not found
        """
        if id not in self.todos:
            return False
        self.todos[id].completed = True
        return True

    def mark_incomplete(self, id: int) -> bool:
        """
        Mark a todo as incomplete by its ID.

        Args:
            id (int): The ID of the todo to mark as incomplete

        Returns:
            bool: True if marked successfully, False if todo not found
        """
        if id not in self.todos:
            return False
        self.todos[id].completed = False
        return True