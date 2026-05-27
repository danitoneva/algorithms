"""
This module finds the missing number in an array between 10 and 20.
"""


class MissingNumberModule:
    """
    This class finds the missing number in an array between 10 and 20.
    """

    def find_missing_number(numbers: int) -> int:
        """
        Finds missing number

        :parameter array
        :return: number
        """
        if len(numbers) != 10:
             raise ValueError("Array lenght must be exactly 10.")
        
        if missing_number < 10 and missing_number > 20:
                raise ValueError("The number should be between 10 and 20.")
        expected_sum = sum(range(10, 21))
        actual_sum = sum(numbers)
        missing_number = expected_sum - actual_sum

        return missing_number
