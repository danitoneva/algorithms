"""
Test for my MissingNumberModule
"""
import unittest
from src.find_missing_number import MissingNumberModule


class TestMissingNumber(unittest.TestCase):
    """This class tests MissingNumberModule"""

    def test_find_first_missing_number(self):
        expected_result = 10
        actual_result = MissingNumberModule.find_missing_number(numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(expected_result, actual_result)

    def test_find_middle_missing_number(self):
        expected_result = 15
        actual_result = MissingNumberModule.find_missing_number(numbers = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
        self.assertEqual(expected_result, actual_result)

    def test_find_last_missing_number(self):
        expected_result = 20
        actual_result = MissingNumberModule.find_missing_number(numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        self.assertEqual(expected_result, actual_result)

    def test_array_not_in_range(self):
        numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,22]
        with self.assertRaises(ValueError):
            MissingNumberModule.find_missing_number(numbers)
