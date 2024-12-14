import unittest
from app import add_task, get_tasks, tasks

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        # Clear the tasks list before each test
        tasks.clear()

    def test_add_task(self):
        add_task("Buy groceries")
        self.assertIn("Buy groceries", get_tasks())

    def test_get_tasks(self):
        add_task("Clean the house")
        add_task("Do homework")
        self.assertEqual(get_tasks(), ["Clean the house", "Do homework"])

if __name__ == '__main__':
    unittest.main()
