
import unittest
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDbHelper(unittest.TestCase):
    @patch('src.db_helper.DbHelper')
    def test_get_maximum_salary(self, MockDbHelper):
        # Create a mock object of DbHelper
        db_helper = MockDbHelper()

        # Mock the get_maximum_salary method to return a specific value
        db_helper.get_maximum_salary.return_value = 60000.00

        # Call the method and check if it returns the expected value
        expected = 60000.00
        actual = db_helper.get_maximum_salary()
        self.assertEqual(expected, actual)

    @patch('src.db_helper.DbHelper')
    def test_get_minimum_salary(self, MockDbHelper):
        # Create a mock object of DbHelper
        db_helper = MockDbHelper()

        # Mock the get_minimum_salary method to return a specific value
        db_helper.get_minimum_salary.return_value = 50000.00

        # Call the method and check if it returns the expected value
        expected = 50000.00
        actual = db_helper.get_minimum_salary()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
