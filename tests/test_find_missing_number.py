"""
Test for my MissingNumberModule
"""
import pytest
from src.find_missing_number import MissingNumberModule


class TestMissingNumber():
    """This class tests MissingNumberModule"""

    def test_find_first_missing_number(self):
        assert MissingNumberModule.find_missing_number([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10

    def test_find_middle_missing_number(self):
        assert MissingNumberModule.find_missing_number([10, 11, 12, 13, 14, 16, 17, 18, 19, 20]) == 15

    def test_find_last_missing_number(self):
        assert MissingNumberModule.find_missing_number([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 20

    def test_array_out_of_space(self):
        assert MissingNumberModule.find_missing_number([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

