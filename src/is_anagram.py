"""
This module checks whether two strings are anagrams.
"""


class AnagramModule:
    """
    This class checks whether two strings are anagrams.
    """

    @staticmethod
    def is_anagram(string1: str, string2: str) -> bool:
        """
        Checks for anagrams.

        :parameter string1: first string
        :parameter string2: second string
        :return: True/False
        """
        if string1.isalpha() and string2.isalpha():
            string1 = string1.lower()
            string2 = string2.lower()
            string1 = "".join(string1.split())
            string2 = "".join(string2.split())
            sorted_string1 = sorted(string1)
            sorted_string2 = sorted(string2)
            if sorted_string1 == sorted_string2:
                return True
            return False
        return False
