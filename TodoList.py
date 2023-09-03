

# Global variable to store the To-Do items
todos = []
class TodoList:


    # Function to add a To-Do item
    def add_todo(task):
        todos.append(task)

    # Function to remove a To-Do item
    def remove_todo(task):
        if task in todos:
            todos.remove(task)

    # Function to list all To-Do items
    def list_todos():
        return todos

    # Function to clear all To-Do items
    def clear_todos():
        global todos
        todos = []

    if __name__ == "__main__":
        while True:
            print("To-Do App")
            print("1. Add To-Do")
            print("2. Remove To-Do")
            print("3. List To-Do")
            print("4. Clear All To-Do")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter the task: ")
                add_todo(task)
                print("Task added successfully!")
            elif choice == "2":
                task = input("Enter the task to remove: ")
                remove_todo(task)
                print("Task removed successfully!")
            elif choice == "3":
                print("To-Do List:")
                for idx, task in enumerate(list_todos(), start=1):
                    print(f"{idx}. {task}")
            elif choice == "4":
                clear_todos()
                print("All tasks cleared!")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")