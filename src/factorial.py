"""
This module finds factorial.
"""


class FactorialModule:
    """
    This class finds factorial 
    """

    @staticmethod
    def factorial(number: int) -> int:
        """
        Finds factorial 

        :parameter number
        :return number
        """
        if number < 0:
            raise ValueError("The number should be equal or greater than 0.")
        if number == 0:
            return 1
        factorial = 1
        for num in range(1,number + 1):
            factorial *= num
        
        return factorial
