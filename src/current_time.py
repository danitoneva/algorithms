"""
This program gets the current time in python.
"""
from datetime import datetime


class CurrentTime:
    "This class gets the current time in python."

    @staticmethod 
    def get_current_time(time: int) -> str:
        """
        Get current time.
        """
        current_time = datetime.now()
        return current_time.strftime("%H:%M:%S.%f")[:-6]
