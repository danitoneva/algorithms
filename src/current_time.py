"""
This program gets the current time in python.
"""
from datetime import datetime, date


class CurrentTime:
    "This class gets the current time in python."

    @staticmethod 
    def get_current_time(current_time: int) -> date:
        """
        Get current time.

        :parameter:time
        """
        current_time = datetime.now()
        return current_time.strftime("%H:%M:%S.%f")[:-6]
