"""
This module checks whether two strings are anagrams.
"""


class AnagramModule:
    """
    This class checks whether two strings are anagrams.
    """

    @staticmethod
    def are_anagrams(string1: str, string2: str) -> bool:
        """
        Checks for anagrams.

        :parameter string1: first string
        :parameter string2: second string
        """
        string1 = string1.lower()
        string2 = string2.lower()
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)
        if sorted_string1 == sorted_string2:
            return True
        else:
            return False