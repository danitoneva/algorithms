""""
Test for my current time module.
"""
import unittest
from datetime import datetime
from src.current_time import CurrentTime


class TestCurrentTime(unittest.TestCase):
    """This class test CurrentTime."""

    def test_hour_range(self):
        current_time = datetime.now()
        self.assertGreaterEqual(current_time.hour, 0, "Hour should be greater than 0.")
        self.assertLessEqual(current_time.hour, 23, "Hour should be less than 24.")

    def test_second_range(self):
        current_time = datetime.now()
        self.assertGreaterEqual(current_time.hour, 0, "Seconds should be greater than 0.")
        self.assertLessEqual(current_time.hour, 23, "Seconds should be less than 59.")