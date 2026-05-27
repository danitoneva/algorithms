"""
This module checks if all characters in a string are unique.
"""


class UniqueModule:
    """
    This class checks if all characters in a string are unique.
    """

    @staticmethod
    def is_unique(string: str) -> bool:
        string = string.lower()
        unique_char = set(string)
        string = list(string)
        if len(unique_char) == len(string):
            return True
        else:
            return False
                