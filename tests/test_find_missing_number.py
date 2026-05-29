"""
Test for my MissingNumberModule
"""
from src.find_missing_number import MissingNumberModule


class TestMissingNumber():
    """This class tests MissingNumberModule"""

    def test_find_first_missing_number(self):
        numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        assert MissingNumberModule.find_missing_number(numbers) == 10

    def test_find_middle_missing_number(self):
        numbers = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
        assert MissingNumberModule.find_missing_number(numbers) == 15

    def test_find_last_missing_number(self):
        numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert MissingNumberModule.find_missing_number(numbers) == 20

    def test_array_out_of_space(self):
        numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        assert MissingNumberModule.find_missing_number(numbers)
