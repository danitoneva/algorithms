"""
Test for my fibonacci module.
"""
import pytest
from src.fibonacci_numbers import FibonacciModule


class TestFibonacciNumbers():
    """This class test the first 10 fibonacci numbers."""

    def test_first_10_fibonacci_numbers(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert FibonacciModule.fibonacci(10) == expected

    def test_negative_numbers(self):
        with pytest.raises(ValueError):
            FibonacciModule.fibonacci(-3)

    def test_more_than_10_numbers(self):
        with pytest.raises(ValueError):
            FibonacciModule.fibonacci(11)

    def test_less_than_10_numbers(self):
        with pytest.raises(ValueError):
            FibonacciModule.fibonacci(9)
