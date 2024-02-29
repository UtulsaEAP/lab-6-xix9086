import unittest
from unittest.mock import patch
from contactlist import process_user_contacts

class TestProcessUserContacts(unittest.TestCase):

    def test_contact_found(self):
        user_input = "Alice 123456 Bob 789012"
        with patch('builtins.input', side_effect=["Bob"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("789012")

    def test_contact_not_found(self):
        user_input = "Alice 123456 Bob 789012"
        with patch('builtins.input', side_effect=["Charlie"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("Contact not found.")

    def test_additional_case(self):
        user_input = "Mo,391-0993 Rachel,019-1265 Ruby,010-8712 Steve,312-3318 Maria,871-0091"
        with patch('builtins.input', side_effect=["Rachel"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("019-1265")

if __name__ == '__main__':
    unittest.main()
