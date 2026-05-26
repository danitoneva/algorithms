"""
This module checks whether two strings are anagrams.
"""

class AnagramModule:
    """
    This class checks whether two strings are anagrams.
    """

    @staticmethod
    def are_anagrams(string1: str, string2: str) -> str:
        """
        Checks for anagrams.

        :parameter string1: first string
        :parameter string2: second string
        """
        reversed_string2 = string2[::-1]
        if string1 == reversed_string2:
            print("The two strings are anagrams.")
        else:
            print("The two strings aren't anagrams.")