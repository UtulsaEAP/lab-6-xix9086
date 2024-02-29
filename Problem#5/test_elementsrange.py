import unittest
from elementsrange import filter_and_print_range

class TestFilterAndPrintRange(unittest.TestCase):
    def test_first_input(self):
        input_list = [25, 51, 0, 200, 33]
        min_val, max_val = 0, 50
        expected_output = "25,0,33,"

        # Redirect stdout to capture the print statements
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to filter and print the range
        filter_and_print_range(input_list, min_val, max_val)

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_second_input(self):
        input_list = [100, 200, 150, 75]
        min_val, max_val = 75, 100
        expected_output = "100,75,"

        # Redirect stdout to capture the print statements
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to filter and print the range
        filter_and_print_range(input_list, min_val, max_val)

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
