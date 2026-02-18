"""
Menu-driven command-line interface and application entry point for the Todo Console Application.
"""
import sys
import os
from typing import Optional

# Add the src directory to the path so imports work when running the script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.todo_service import TodoService


# Menu constants and configuration
MENU_OPTIONS = {
    1: "Add a new task",
    2: "View all tasks",
    3: "Update a task",
    4: "Delete a task",
    5: "Mark task as complete",
    6: "Mark task as incomplete",
    7: "Exit"
}

MENU_HEADER = """
================================
  TODO CONSOLE APPLICATION
================================
"""


class TodoCLI:
    """
    Command-line interface for the Todo application.
    """

    def __init__(self):
        """
        Initialize the CLI with a TodoService instance.
        """
        self.service = TodoService()

    def run(self):
        """
        Run the main application loop with menu-driven interface.
        """
        while True:
            try:
                # Display menu header and options
                print(MENU_HEADER)
                print("Please select an option:")
                for option_num, option_desc in MENU_OPTIONS.items():
                    print(f"{option_num}. {option_desc}")

                user_input = input("\nEnter your choice (1-7): ").strip()

                if not user_input:
                    continue

                try:
                    choice = int(user_input)
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 7.")
                    continue

                if choice == 1:
                    self.handle_add_menu()
                elif choice == 2:
                    self.handle_view_menu()
                elif choice == 3:
                    self.handle_update_menu()
                elif choice == 4:
                    self.handle_delete_menu()
                elif choice == 5:
                    self.handle_complete_menu()
                elif choice == 6:
                    self.handle_incomplete_menu()
                elif choice == 7:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 7.")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def handle_command(self, command: str, args: list):
        """
        Route user input to corresponding service methods.

        Args:
            command (str): The command to execute
            args (list): Arguments for the command
        """
        try:
            if command == "add":
                self.handle_add(args)
            elif command == "view":
                self.handle_view()
            elif command == "update":
                self.handle_update(args)
            elif command == "delete":
                self.handle_delete(args)
            elif command == "complete":
                self.handle_complete(args)
            elif command == "incomplete":
                self.handle_incomplete(args)
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")
        except Exception as e:
            print(f"Error: {e}")

    def handle_add(self, args: list):
        """
        Handle the 'add' command.

        Args:
            args (list): Arguments for the add command [title, description]
        """
        if len(args) < 1:
            print("Usage: add \"title\" [\"description\"]")
            return

        title = args[0].strip('"')
        description = None
        if len(args) > 1:
            description = args[1].strip('"')

        try:
            todo_id = self.service.add_todo(title, description)
            if todo_id is not None:
                print(f"Added todo #{todo_id}: {title}")
            else:
                print("Failed to add todo.")
        except ValueError as e:
            print(f"Error adding todo: {e}")

    def handle_view(self, args: list = None):
        """
        Handle the 'view' command.

        Args:
            args (list, optional): Arguments for the view command (none expected)
        """
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos found.")
        else:
            for todo in todos:
                print(todo)

    def handle_update(self, args: list):
        """
        Handle the 'update' command.

        Args:
            args (list): Arguments for the update command [id, title, description]
        """
        if len(args) < 2:
            print("Usage: update <id> \"new title\" [\"new description\"]")
            return

        try:
            id = int(args[0])
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        title = args[1].strip('"')
        description = None
        if len(args) > 2:
            description = args[2].strip('"')

        success = self.service.update_todo(id, title, description)
        if success:
            print(f"Updated todo #{id}")
        else:
            print(f"Todo with ID #{id} not found.")

    def handle_delete(self, args: list):
        """
        Handle the 'delete' command.

        Args:
            args (list): Arguments for the delete command [id]
        """
        if len(args) < 1:
            print("Usage: delete <id>")
            return

        try:
            id = int(args[0])
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        success = self.service.delete_todo(id)
        if success:
            print(f"Deleted todo #{id}")
        else:
            print(f"Todo with ID #{id} not found.")

    def handle_complete(self, args: list):
        """
        Handle the 'complete' command.

        Args:
            args (list): Arguments for the complete command [id]
        """
        if len(args) < 1:
            print("Usage: complete <id>")
            return

        try:
            id = int(args[0])
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        success = self.service.mark_complete(id)
        if success:
            print(f"Marked todo #{id} as complete")
        else:
            print(f"Todo with ID #{id} not found.")

    def handle_incomplete(self, args: list):
        """
        Handle the 'incomplete' command.

        Args:
            args (list): Arguments for the incomplete command [id]
        """
        if len(args) < 1:
            print("Usage: incomplete <id>")
            return

        try:
            id = int(args[0])
        except ValueError:
            print("Invalid ID. Please provide a numeric ID.")
            return

        success = self.service.mark_incomplete(id)
        if success:
            print(f"Marked todo #{id} as incomplete")
        else:
            print(f"Todo with ID #{id} not found.")

    def show_help(self):
        """
        Display help information for available commands.
        """
        help_text = """
Available commands:
  add "title" ["description"]    - Add a new todo
  view                          - View all todos
  update <id> "title" ["desc"]  - Update a todo
  delete <id>                   - Delete a todo
  complete <id>                 - Mark todo as complete
  incomplete <id>               - Mark todo as incomplete
  help                          - Show this help message
  exit                          - Exit the application
        """
        print(help_text)

    def handle_add_menu(self):
        """
        Handle the 'Add a new task' menu option with guided prompts.
        """
        try:
            print("\n--- Add New Task ---")
            title = input("Enter task title: ").strip()
            if not title:
                print("Title cannot be empty.")
                input("\nPress Enter to return to the main menu...")
                return

            description_input = input("Enter task description (optional, press Enter to skip): ").strip()
            description = description_input if description_input else None

            todo_id = self.service.add_todo(title, description)
            if todo_id is not None:
                print(f"Added task #{todo_id}: {title}")
            else:
                print("Failed to add task.")
            input("\nPress Enter to return to the main menu...")
        except ValueError as e:
            print(f"Error adding task: {e}")
            input("\nPress Enter to return to the main menu...")

    def handle_view_menu(self):
        """
        Handle the 'View all tasks' menu option.
        """
        todos = self.service.get_all_todos()
        if not todos:
            print("\nNo tasks found.")
            input("\nPress Enter to return to the main menu...")
        else:
            print("\nYour tasks:")
            print("-" * 60)
            for todo in todos:
                print(todo)
            print("-" * 60)
            input("\nPress Enter to return to the main menu...")

    def handle_update_menu(self):
        """
        Handle the 'Update a task' menu option with guided prompts.
        """
        try:
            print("\n--- Update Task ---")
            id_input = input("Enter task ID to update: ").strip()
            if not id_input:
                print("Task ID cannot be empty.")
                input("\nPress Enter to return to the main menu...")
                return

            try:
                id = int(id_input)
            except ValueError:
                print("Invalid ID. Please provide a numeric ID.")
                input("\nPress Enter to return to the main menu...")
                return

            title = input("Enter new task title: ").strip()
            if not title:
                print("Title cannot be empty.")
                input("\nPress Enter to return to the main menu...")
                return

            description_input = input("Enter new task description (optional, press Enter to skip): ").strip()
            description = description_input if description_input else None

            success = self.service.update_todo(id, title, description)
            if success:
                print(f"Updated task #{id}")
            else:
                print(f"Task with ID #{id} not found.")
            input("\nPress Enter to return to the main menu...")
        except ValueError as e:
            print(f"Error updating task: {e}")
            input("\nPress Enter to return to the main menu...")

    def handle_delete_menu(self):
        """
        Handle the 'Delete a task' menu option with guided prompts.
        """
        try:
            print("\n--- Delete Task ---")
            id_input = input("Enter task ID to delete: ").strip()
            if not id_input:
                print("Task ID cannot be empty.")
                input("\nPress Enter to return to the main menu...")
                return

            try:
                id = int(id_input)
            except ValueError:
                print("Invalid ID. Please provide a numeric ID.")
                input("\nPress Enter to return to the main menu...")
                return

            success = self.service.delete_todo(id)
            if success:
                print(f"Deleted task #{id}")
            else:
                print(f"Task with ID #{id} not found.")
            input("\nPress Enter to return to the main menu...")
        except ValueError as e:
            print(f"Error deleting task: {e}")
            input("\nPress Enter to return to the main menu...")

    def handle_complete_menu(self):
        """
        Handle the 'Mark task as complete' menu option with guided prompts.
        """
        try:
            print("\n--- Mark Task Complete ---")
            id_input = input("Enter task ID to mark as complete: ").strip()
            if not id_input:
                print("Task ID cannot be empty.")
                input("\nPress Enter to return to the main menu...")
                return

            try:
                id = int(id_input)
            except ValueError:
                print("Invalid ID. Please provide a numeric ID.")
                input("\nPress Enter to return to the main menu...")
                return

            success = self.service.mark_complete(id)
            if success:
                print(f"Marked task #{id} as complete")
            else:
                print(f"Task with ID #{id} not found.")
            input("\nPress Enter to return to the main menu...")
        except ValueError as e:
            print(f"Error marking task as complete: {e}")
            input("\nPress Enter to return to the main menu...")

    def handle_incomplete_menu(self):
        """
        Handle the 'Mark task as incomplete' menu option with guided prompts.
        """
        try:
            print("\n--- Mark Task Incomplete ---")
            id_input = input("Enter task ID to mark as incomplete: ").strip()
            if not id_input:
                print("Task ID cannot be empty.")
                input("\nPress Enter to return to the main menu...")
                return

            try:
                id = int(id_input)
            except ValueError:
                print("Invalid ID. Please provide a numeric ID.")
                input("\nPress Enter to return to the main menu...")
                return

            success = self.service.mark_incomplete(id)
            if success:
                print(f"Marked task #{id} as incomplete")
            else:
                print(f"Task with ID #{id} not found.")
            input("\nPress Enter to return to the main menu...")
        except ValueError as e:
            print(f"Error marking task as incomplete: {e}")
            input("\nPress Enter to return to the main menu...")


def main():
    """
    Entry point for the application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()