
import unittest
from app import greet_user, add_numbers, multiply_numbers

class TestApp(unittest.TestCase):

    def test_greet_user(self):
        self.assertEqual(greet_user("Alice"), "Hello, Alice! Welcome to Lab 4 Python CI workflow.")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 5), 20)

if __name__ == "__main__":
    unittest.main()
