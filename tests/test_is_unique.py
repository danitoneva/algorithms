"""
Test for my UniqueModule.
"""
import unittest
from src.is_unique import UniqueModule


class TestIsUnique(unittest.TestCase):
    """This class test my UniqueModule"""

    def test_is_unique(self):
        expected_result = True
        actual_result = UniqueModule.is_unique(string = "abcd")
        self.assertEqual(expected_result, actual_result)

    def test_is_unique_with_digit(self):
        expected_result = True
        actual_result = UniqueModule.is_unique(string = "abcd9")
        self.assertEqual(expected_result, actual_result)

    def test_is_not_unique(self):
        expected_result = False
        actual_result = UniqueModule.is_unique(string = "abcddc")
        self.assertEqual(expected_result, actual_result)

    def test_is_not_unique_with_digit(self):
        expected_result = False
        actual_result = UniqueModule.is_unique(string = "ab1cd1")
        self.assertEqual(expected_result, actual_result)

    def test_is_unique_with_capital(self):
        expected_result = True
        actual_result = UniqueModule.is_unique(string = "aBcd")
        self.assertEqual(expected_result, actual_result)

    def test_is_not_unique_with_capital(self):
        expected_result = False
        actual_result = UniqueModule.is_unique(string = "aBcDD")
        self.assertEqual(expected_result, actual_result)
