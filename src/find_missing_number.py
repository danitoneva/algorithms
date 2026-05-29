"""
This module finds the missing number in an array between 10 and 20.
"""


class MissingNumberModule:
    """
    This class finds the missing number in an array between 10 and 20.
    """

    @staticmethod
    def find_missing_number(numbers: int) -> int:
        """
        Finds missing number

        :parameter array
        :return: number
        """
        if len(numbers) != 10:
            raise ValueError("Array lenght must be exactly 10.")
        expected_sum = sum(range(10, 21))
        actual_sum = sum(numbers)
        missing_number = expected_sum - actual_sum
        if 20 < missing_number < 10:
            raise ValueError("The number should be between 10 and 20.")

        return missing_number
