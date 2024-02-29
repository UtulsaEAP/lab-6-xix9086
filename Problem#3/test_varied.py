import unittest
from varied import process_input

class TestProcessInput(unittest.TestCase):
    def test_case_1(self):
        input_string = "14.25 25 0 5.75"
        max_value, average_value = process_input(input_string)
        self.assertEqual(max_value, 25.00)
        self.assertEqual(average_value, 11.25)

    def test_case_2(self):
        input_string = "2 2 2 2 12 0 8 4"
        max_value, average_value = process_input(input_string)
        self.assertEqual(max_value, 12.00)
        self.assertEqual(average_value, 4.00)

if __name__ == "__main__":
    unittest.main()
