"""
Test for my factorial module.
"""
import pytest
from src.factorial import FactorialModule

class TestFactorialModule():
    """Class test FactorialModule"""

    def test_factorial_negative_number(self):
        assert FactorialModule.factorial(-1) 

    def test_factorial_with_one(self):
        assert FactorialModule.factorial(0) == 1

    def test_factorial_positive_number(self):
        assert FactorialModule.factorial(4) == 24
