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
        Gives 
        """
        if number != 10:
            raise ValueError("It should print the first 10 numbers.")
        if number < 0:
            raise ValueError("This number should be non-negative.")
        numbers = []
        first_number, second_number = 0, 1
        for num in range(10):
            numbers.append(first_number)
            first_number, second_number = second_number, first_number + second_number
        return numbers    
