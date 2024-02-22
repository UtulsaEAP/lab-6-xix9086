import unittest
from filter import process_and_print

class TestProcessAndPrint(unittest.TestCase):
    def test_positive_input(self):
        user_input = "10 -7 4 -39 -6 12 -2"
        expected_output = "-2 -6 -7 -39 "
        
        # Redirect stdout to capture the print statements
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function to process and print
        process_and_print(user_input)
        
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_negative_input(self):
        user_input = "-25"
        expected_output = "-25 "
        
        # Redirect stdout to capture the print statements
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function to process and print
        process_and_print(user_input)
        
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_another_negative_input(self):
        user_input = "-3 -99 -3 -1 -27"
        expected_output = "-1 -3 -3 -27 -99 "
        
        # Redirect stdout to capture the print statements
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function to process and print
        process_and_print(user_input)
        
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
