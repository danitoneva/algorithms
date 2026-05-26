"""
Test for my anagram module.
"""
import unittest
from src.are_anagrams import AnagramModule


class TestAnagramModule(unittest.TestCase):
    """
    This class tests my AnagramModule.
    """

    def test_two_strings_anagrams(self):
        expected_result = True
        actual_result = AnagramModule.are_anagrams(string1= "grpko", string2= "orpgk")
        self.assertEqual(expected_result, actual_result)

    def test_two_strings_anagrams_capital_letter(self):
        expected_result = True
        actual_result = AnagramModule.are_anagrams(string1= "gRpko", string2= "orpgK")
        self.assertEqual(expected_result, actual_result)