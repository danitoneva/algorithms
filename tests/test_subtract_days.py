"""
Test for my subract module.
"""
from datetime import date, timedelta
from src.subtract_days import SubtractModule


class TestSubtractDays():
    """This class tests the subtracting 5 days from the current day."""

    def test_subract_5_days(self):
        current_date = date.today()
        expected_date = current_date - timedelta(days=5)
        assert SubtractModule.subtract_days_from_current_date(5) == expected_date

    def test_subract_4_days(self):
        current_date = date.today()
        expected_date = current_date - timedelta(days=4)
        assert SubtractModule.subtract_days_from_current_date(4) == expected_date

    def test_subract_6_days(self):
        current_date = date.today()
        expected_date = current_date - timedelta(days=6)
        assert SubtractModule.subtract_days_from_current_date(6) == expected_date
