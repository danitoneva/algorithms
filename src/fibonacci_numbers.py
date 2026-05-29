"""
This module prints first 10 fibonacci numbers.
"""


class FibonacciModule:
    """"
    This class prints fisrt 10 fibonacci numbers.
    """

    @staticmethod
    def fibonacci(number: int) -> int:
        """
        Gives first 10 fibonacci numbers.
        """
        if number != 10:
            raise ValueError("It should print the first 10 numbers.")
        if number < 0:
            raise ValueError("This number should be non-negative.")
        return FibonacciModule.fibonacci(number - 1) + FibonacciModule.fibonacci(number -2 )
