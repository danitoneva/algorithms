"""
Test for my factorial module.
"""
import pytest
from src.factorial_second_way import SecondFactorialModule

class TestSecondFactorialModule():
    """Class test FactorialModule"""

    def test_factorial_negative_number(self):
        assert SecondFactorialModule.factorial_second(-1) 

    def test_factorial_with_one(self):
        assert SecondFactorialModule.factorial_second(0) == 1

    def test_factorial_positive_number(self):
        assert SecondFactorialModule.factorial_second(4) == 24