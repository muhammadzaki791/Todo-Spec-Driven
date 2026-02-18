"""
Unit tests for todo functionality.
"""
import unittest
from src.models.todo import Todo, TodoList
from src.services.todo_service import TodoService


class TestTodo(unittest.TestCase):
    """
    Test cases for the Todo class.
    """

    def test_todo_creation_valid(self):
        """
        Test creating a valid Todo object.
        """
        todo = Todo(id=1, title="Test title", description="Test description", completed=False)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test title")
        self.assertEqual(todo.description, "Test description")
        self.assertFalse(todo.completed)

    def test_todo_creation_defaults(self):
        """
        Test creating a Todo object with default values.
        """
        todo = Todo(id=1, title="Test title")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test title")
        self.assertIsNone(todo.description)
        self.assertFalse(todo.completed)

    def test_todo_creation_completed(self):
        """
        Test creating a Todo object with completed status.
        """
        todo = Todo(id=1, title="Test title", completed=True)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test title")
        self.assertTrue(todo.completed)

    def test_todo_title_required(self):
        """
        Test that Todo creation fails with empty title.
        """
        with self.assertRaises(ValueError):
            Todo(id=1, title="")

    def test_todo_title_whitespace_only(self):
        """
        Test that Todo creation fails with whitespace-only title.
        """
        with self.assertRaises(ValueError):
            Todo(id=1, title="   ")

    def test_todo_title_length_limit(self):
        """
        Test that Todo creation fails with title exceeding 200 characters.
        """
        long_title = "a" * 201
        with self.assertRaises(ValueError):
            Todo(id=1, title=long_title)

    def test_todo_description_length_limit(self):
        """
        Test that Todo creation fails with description exceeding 1000 characters.
        """
        long_description = "a" * 1001
        with self.assertRaises(ValueError):
            Todo(id=1, title="Test", description=long_description)

    def test_todo_string_representation(self):
        """
        Test the string representation of a Todo object.
        """
        todo = Todo(id=1, title="Test title", description="Test description", completed=True)
        expected = "1. [x] Test title - Test description"
        self.assertEqual(str(todo), expected)

    def test_todo_string_representation_no_description(self):
        """
        Test the string representation of a Todo object without description.
        """
        todo = Todo(id=1, title="Test title", completed=False)
        expected = "1. [ ] Test title"
        self.assertEqual(str(todo), expected)


class TestTodoList(unittest.TestCase):
    """
    Test cases for the TodoList class.
    """

    def setUp(self):
        """
        Set up a TodoList instance for testing.
        """
        self.todo_list = TodoList()

    def test_add_todo_success(self):
        """
        Test adding a todo successfully.
        """
        todo = Todo(id=1, title="Test title")
        result = self.todo_list.add_todo(todo)
        self.assertTrue(result)
        self.assertIn(1, self.todo_list.todos)
        self.assertEqual(self.todo_list.todos[1], todo)

    def test_add_todo_duplicate_id(self):
        """
        Test that adding a todo with duplicate ID fails.
        """
        todo1 = Todo(id=1, title="Test title 1")
        todo2 = Todo(id=1, title="Test title 2")

        self.todo_list.add_todo(todo1)
        result = self.todo_list.add_todo(todo2)
        self.assertFalse(result)

    def test_get_todo_exists(self):
        """
        Test getting an existing todo.
        """
        todo = Todo(id=1, title="Test title")
        self.todo_list.add_todo(todo)

        retrieved = self.todo_list.get_todo(1)
        self.assertEqual(retrieved, todo)

    def test_get_todo_not_exists(self):
        """
        Test getting a non-existing todo.
        """
        result = self.todo_list.get_todo(999)
        self.assertIsNone(result)

    def test_get_all_todos(self):
        """
        Test getting all todos.
        """
        todo1 = Todo(id=1, title="Test title 1")
        todo2 = Todo(id=2, title="Test title 2")

        self.todo_list.add_todo(todo1)
        self.todo_list.add_todo(todo2)

        all_todos = self.todo_list.get_all_todos()
        self.assertEqual(len(all_todos), 2)
        self.assertIn(todo1, all_todos)
        self.assertIn(todo2, all_todos)

    def test_update_todo_success(self):
        """
        Test updating a todo successfully.
        """
        todo = Todo(id=1, title="Old title", description="Old description")
        self.todo_list.add_todo(todo)

        result = self.todo_list.update_todo(1, title="New title", description="New description")
        self.assertTrue(result)
        self.assertEqual(todo.title, "New title")
        self.assertEqual(todo.description, "New description")

    def test_update_todo_not_exists(self):
        """
        Test updating a non-existing todo.
        """
        result = self.todo_list.update_todo(999, title="New title")
        self.assertFalse(result)

    def test_update_todo_title_only(self):
        """
        Test updating only the title of a todo.
        """
        todo = Todo(id=1, title="Old title", description="Old description")
        self.todo_list.add_todo(todo)

        result = self.todo_list.update_todo(1, title="New title")
        self.assertTrue(result)
        self.assertEqual(todo.title, "New title")
        self.assertEqual(todo.description, "Old description")

    def test_update_todo_description_only(self):
        """
        Test updating only the description of a todo.
        """
        todo = Todo(id=1, title="Old title", description="Old description")
        self.todo_list.add_todo(todo)

        result = self.todo_list.update_todo(1, description="New description")
        self.assertTrue(result)
        self.assertEqual(todo.title, "Old title")
        self.assertEqual(todo.description, "New description")

    def test_delete_todo_success(self):
        """
        Test deleting a todo successfully.
        """
        todo = Todo(id=1, title="Test title")
        self.todo_list.add_todo(todo)

        result = self.todo_list.delete_todo(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.todo_list.todos)

    def test_delete_todo_not_exists(self):
        """
        Test deleting a non-existing todo.
        """
        result = self.todo_list.delete_todo(999)
        self.assertFalse(result)

    def test_mark_complete_success(self):
        """
        Test marking a todo as complete.
        """
        todo = Todo(id=1, title="Test title", completed=False)
        self.todo_list.add_todo(todo)

        result = self.todo_list.mark_complete(1)
        self.assertTrue(result)
        self.assertTrue(todo.completed)

    def test_mark_complete_not_exists(self):
        """
        Test marking a non-existing todo as complete.
        """
        result = self.todo_list.mark_complete(999)
        self.assertFalse(result)

    def test_mark_incomplete_success(self):
        """
        Test marking a todo as incomplete.
        """
        todo = Todo(id=1, title="Test title", completed=True)
        self.todo_list.add_todo(todo)

        result = self.todo_list.mark_incomplete(1)
        self.assertTrue(result)
        self.assertFalse(todo.completed)

    def test_mark_incomplete_not_exists(self):
        """
        Test marking a non-existing todo as incomplete.
        """
        result = self.todo_list.mark_incomplete(999)
        self.assertFalse(result)


class TestTodoService(unittest.TestCase):
    """
    Test cases for the TodoService class.
    """

    def setUp(self):
        """
        Set up a TodoService instance for testing.
        """
        self.service = TodoService()

    def test_add_todo_success(self):
        """
        Test adding a todo successfully through the service.
        """
        result = self.service.add_todo("Test title", "Test description")
        self.assertIsNotNone(result)
        self.assertEqual(result, 1)  # First todo should have ID 1

        # Verify the todo was added
        todo = self.service.get_todo(1)
        self.assertIsNotNone(todo)
        self.assertEqual(todo.title, "Test title")
        self.assertEqual(todo.description, "Test description")
        self.assertFalse(todo.completed)

    def test_add_todo_no_description(self):
        """
        Test adding a todo without description.
        """
        result = self.service.add_todo("Test title")
        self.assertIsNotNone(result)
        self.assertEqual(result, 1)

        todo = self.service.get_todo(1)
        self.assertIsNotNone(todo)
        self.assertEqual(todo.title, "Test title")
        self.assertIsNone(todo.description)

    def test_add_todo_validation(self):
        """
        Test that adding a todo with empty title fails validation.
        """
        with self.assertRaises(ValueError):
            self.service.add_todo("")

    def test_get_all_todos_empty(self):
        """
        Test getting all todos when the list is empty.
        """
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_get_all_todos_with_items(self):
        """
        Test getting all todos when the list has items.
        """
        self.service.add_todo("Title 1", "Description 1")
        self.service.add_todo("Title 2", "Description 2")

        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 2)

    def test_update_todo_success(self):
        """
        Test updating a todo successfully.
        """
        self.service.add_todo("Old title", "Old description")

        result = self.service.update_todo(1, "New title", "New description")
        self.assertTrue(result)

        updated_todo = self.service.get_todo(1)
        self.assertEqual(updated_todo.title, "New title")
        self.assertEqual(updated_todo.description, "New description")

    def test_update_todo_not_exists(self):
        """
        Test updating a non-existing todo.
        """
        result = self.service.update_todo(999, "New title")
        self.assertFalse(result)

    def test_delete_todo_success(self):
        """
        Test deleting a todo successfully.
        """
        self.service.add_todo("Test title")

        result = self.service.delete_todo(1)
        self.assertTrue(result)

        todo = self.service.get_todo(1)
        self.assertIsNone(todo)

    def test_delete_todo_not_exists(self):
        """
        Test deleting a non-existing todo.
        """
        result = self.service.delete_todo(999)
        self.assertFalse(result)

    def test_mark_complete_success(self):
        """
        Test marking a todo as complete.
        """
        self.service.add_todo("Test title")

        result = self.service.mark_complete(1)
        self.assertTrue(result)

        todo = self.service.get_todo(1)
        self.assertTrue(todo.completed)

    def test_mark_complete_not_exists(self):
        """
        Test marking a non-existing todo as complete.
        """
        result = self.service.mark_complete(999)
        self.assertFalse(result)

    def test_mark_incomplete_success(self):
        """
        Test marking a todo as incomplete.
        """
        self.service.add_todo("Test title")
        self.service.mark_complete(1)  # Mark as complete first

        result = self.service.mark_incomplete(1)
        self.assertTrue(result)

        todo = self.service.get_todo(1)
        self.assertFalse(todo.completed)

    def test_mark_incomplete_not_exists(self):
        """
        Test marking a non-existing todo as incomplete.
        """
        result = self.service.mark_incomplete(999)
        self.assertFalse(result)

    def test_validate_todo_exists(self):
        """
        Test validating if a todo exists.
        """
        self.service.add_todo("Test title")

        self.assertTrue(self.service.validate_todo_exists(1))
        self.assertFalse(self.service.validate_todo_exists(999))


if __name__ == '__main__':
    unittest.main()