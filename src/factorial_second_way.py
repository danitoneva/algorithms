""""
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
        return (number * factorial(number - 1))