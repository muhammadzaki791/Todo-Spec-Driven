"""
Core business logic for todo operations.
"""
from typing import Optional, List
from src.models.todo import Todo, TodoList


class TodoService:
    """
    Service class containing the core business logic for todo operations.
    """

    def __init__(self):
        """
        Initialize the TodoService with an empty TodoList.
        """
        self.todo_list = TodoList()
        self._next_id = 1

    def add_todo(self, title: str, description: Optional[str] = None) -> Optional[int]:
        """
        Add a new todo to the collection.

        Args:
            title (str): Title of the todo (required)
            description (str, optional): Description of the todo (optional)

        Returns:
            int: The ID of the newly created todo, or None if failed
        """
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Title must be provided and not empty")

        if len(title) > 200:
            raise ValueError("Title must not exceed 200 characters")

        if description and len(description) > 1000:
            raise ValueError("Description must not exceed 1000 characters")

        # Create a new Todo with the next available ID
        todo = Todo(id=self._next_id, title=title, description=description)
        success = self.todo_list.add_todo(todo)

        if success:
            # Increment the ID counter for the next todo
            self._next_id += 1
            return todo.id
        else:
            # This should not happen with auto-generated IDs, but just in case
            return None

    def get_todo(self, id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            id (int): The ID of the todo to retrieve

        Returns:
            Todo: The Todo object if found, None otherwise
        """
        return self.todo_list.get_todo(id)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the collection.

        Returns:
            list: List of all Todo objects
        """
        return self.todo_list.get_all_todos()

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
        # Validate inputs if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title must be provided and not empty")
            if len(title) > 200:
                raise ValueError("Title must not exceed 200 characters")

        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description must not exceed 1000 characters")

        return self.todo_list.update_todo(id, title, description)

    def delete_todo(self, id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            id (int): The ID of the todo to delete

        Returns:
            bool: True if deleted successfully, False if todo not found
        """
        return self.todo_list.delete_todo(id)

    def mark_complete(self, id: int) -> bool:
        """
        Mark a todo as complete by its ID.

        Args:
            id (int): The ID of the todo to mark as complete

        Returns:
            bool: True if marked successfully, False if todo not found
        """
        return self.todo_list.mark_complete(id)

    def mark_incomplete(self, id: int) -> bool:
        """
        Mark a todo as incomplete by its ID.

        Args:
            id (int): The ID of the todo to mark as incomplete

        Returns:
            bool: True if marked successfully, False if todo not found
        """
        return self.todo_list.mark_incomplete(id)

    def validate_todo_exists(self, id: int) -> bool:
        """
        Check if a todo with the given ID exists.

        Args:
            id (int): The ID to check

        Returns:
            bool: True if the todo exists, False otherwise
        """
        return self.todo_list.get_todo(id) is not None