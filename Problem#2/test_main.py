import unittest
from main import check_palindrome
import io
import unittest.mock

class TestCheckPalindrome(unittest.TestCase):

    def test_palindrome(self):
        user_input = "bob"
        expected_output = "palindrome: bob"

        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_not_palindrome(self):
        user_input = "statistics"
        expected_output = "not a palindrome: statistics"

        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
