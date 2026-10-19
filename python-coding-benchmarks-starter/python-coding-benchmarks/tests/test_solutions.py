"""Unit tests for the reference solutions."""

import unittest

from src.solutions import count_vowels, is_palindrome, find_missing_number


class TestCountVowels(unittest.TestCase):
    def test_counts_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_is_case_insensitive(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("Race car"))

    def test_ignores_punctuation_and_spaces(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("python"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


class TestFindMissingNumber(unittest.TestCase):
    def test_missing_middle_number(self):
        self.assertEqual(find_missing_number([3, 0, 1]), 2)

    def test_missing_last_number(self):
        self.assertEqual(find_missing_number([0, 1]), 2)

    def test_missing_zero(self):
        self.assertEqual(find_missing_number([1]), 0)

    def test_empty_list(self):
        self.assertEqual(find_missing_number([]), 0)


if __name__ == "__main__":
    unittest.main()
