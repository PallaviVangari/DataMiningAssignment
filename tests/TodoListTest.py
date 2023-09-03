import sys
import unittest

#navigate to the parent directory and import the TodoList module
sys.path.append("..")
from TodoList import TodoList

class TodoNodeTest(unittest.TestCase):

    def setUp(self):
        # Initialize the todos before each test
        TodoList.clear_todos()

    def test_add_todo(self):
        TodoList.add_todo("Task 1")
        self.assertIn("Task 1", TodoList.list_todos())

    def test_remove_todo(self):
        TodoList.add_todo("Task 1")
        TodoList.remove_todo("Task 1")
        self.assertNotIn("Task 1", TodoList.list_todos())

    def test_list_todos(self):
        TodoList.add_todo("Task 1")
        TodoList.add_todo("Task 2")
        self.assertEqual(TodoList.list_todos(), ["Task 1", "Task 2"])

    def test_clear_todos(self):
        TodoList.add_todo("Task 1")
        TodoList.clear_todos()
        self.assertEqual(TodoList.list_todos(), [])

if __name__ == '__main__':
    unittest.main()