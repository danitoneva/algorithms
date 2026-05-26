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
        actual_result = AnagramModule.are_anagrams(string1= "string", string2= "irgnts")
        self.assertEqual(expected_result, actual_result)

    def test_two_strings_anagrams_capital_letter(self):
        expected_result = True
        actual_result = AnagramModule.are_anagrams(string1= "String", string2= "irgnTs")
        self.assertEqual(expected_result, actual_result)

    def test_two_strings_anagrams_with_space(self):
        expected_result = True
        actual_result = AnagramModule.are_anagrams(string1= "st ring", string2= "string")
        self.assertEqual(expected_result, actual_result)

    def test_two_strings_anagrams_with_space_and_capital(self):
        expected_result = True
        actual_result = AnagramModule.are_anagrams(string1= "sT ring", string2= "stRi ng")
        self.assertEqual(expected_result, actual_result)

    def test_two_strings_anagrams_with_symbol(self):
        expected_result = False
        actual_result = AnagramModule.are_anagrams(string1= "string)", string2= "str*ing")
        self.assertEqual(expected_result, actual_result)
