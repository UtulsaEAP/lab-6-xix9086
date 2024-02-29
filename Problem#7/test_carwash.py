from io import StringIO
import sys
from unittest import TestCase
import unittest
from unittest.mock import patch

# Import the function from the main module
from carwash import calculate_car_wash_price

class TestCalculateCarWashPrice(TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def assert_output(self, expected_output):
        actual_output = self.held_output.getvalue().strip()
        self.assertEqual(actual_output, expected_output.strip())

    def test_case_1(self):
        with patch('builtins.input', side_effect=["-", "-"]):
            calculate_car_wash_price("-", "-")
        self.assert_output("""
ZyCar Wash
Base car wash - $10
-----
Total price: $10
        """)

    def test_case_2(self):
        with patch('builtins.input', side_effect=["Tire shine", "Wax"]):
            calculate_car_wash_price("Tire shine", "Wax")
        self.assert_output("""
ZyCar Wash
Base car wash - $10
Tire shine - $2
Wax - $3
-----
Total price: $15
        """)

    def test_case_3(self):
        with patch('builtins.input', side_effect=["Rain repellent", "-"]):
            calculate_car_wash_price("Rain repellent", "-")
        self.assert_output("""
ZyCar Wash
Base car wash - $10
Rain repellent - $2
-----
Total price: $12
        """)

# Run the tests
if __name__ == '__main__':
    unittest.main()
