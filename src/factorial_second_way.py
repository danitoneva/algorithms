""""
This module finds factorial.
"""


class SecondFactorialModule:
    """
    This class finds factorial 
    """

    @staticmethod
    def factorial_second(number: int) -> int:
        """
        Finds factorial 

        :parameter number
        :return number
        """
        if number < 0:
            raise ValueError("The number should be equal or greater than 0.")
        if number == 0:
            return 1
        return number * SecondFactorialModule.factorial_second(number-1)
