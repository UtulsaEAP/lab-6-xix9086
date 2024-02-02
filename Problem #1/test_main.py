import unittest
from unittest.mock import patch
from io import StringIO
from main import food_input

class TestFoodInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["cars 99", "quit 0"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_case1(self, mock_stdout, mock_input):
        food_input()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Eating 99 cars a day keeps you happy and healthy.\n"
        )

    @patch("builtins.input", side_effect=["apples 5", "shoes 2", "quit 0"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_case2(self, mock_stdout, mock_input):
        food_input()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Eating 5 apples a day keeps you happy and healthy.\n"
            "Eating 2 shoes a day keeps you happy and healthy.\n"
        )

if __name__ == "__main__":
    unittest.main()
