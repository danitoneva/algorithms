"""
Module that subtracts 5 days from the current date.
"""
from datetime import date, timedelta


class SubtractModule:
    """This class subtracts 5 days from the current date."""

    @staticmethod
    def subtract_days_from_current_date():
        """
        Subtracts 5 days from the current date.

        :parameter: date
        :return:
        """
        return date.today() - timedelta(days = 5)
