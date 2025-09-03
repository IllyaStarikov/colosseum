#!/usr/bin/env python3
"""
https://leetcode.com/problems/valid-word-abbreviation/

Author: Illya Starikov
Date: 2025-08-29
License: MIT
"""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
solution_module = __import__("408_valid_word_abbreviation")


class TestValidWordAbbreviation(unittest.TestCase):
    def setUp(self):
        self.solution = solution_module.Solution()

    def test_valid_abbreviation(self):
        """Test valid abbreviation with multiple numbers"""
        self.assertTrue(
            self.solution.validWordAbbreviation('internationalization', 'i12iz4n')
        )

    def test_invalid_abbreviation(self):
        """Test invalid abbreviation - doesn't match the word"""
        self.assertFalse(
            self.solution.validWordAbbreviation('apple', 'a2e')
        )

    # CLAUDE-CODE BEGIN

    def test_leading_zero_invalid(self):
        """Leading zeros should make abbreviation invalid"""
        self.assertFalse(
            self.solution.validWordAbbreviation('apple', 'a03e')
        )
        self.assertFalse(
            self.solution.validWordAbbreviation('word', 'w01d')
        )

    def test_exact_match_no_numbers(self):
        """Abbreviation with no numbers should match exactly"""
        self.assertTrue(
            self.solution.validWordAbbreviation('apple', 'apple')
        )
        self.assertFalse(
            self.solution.validWordAbbreviation('apple', 'appla')
        )

    def test_single_number_abbreviations(self):
        """Test single number replacements"""
        self.assertTrue(
            self.solution.validWordAbbreviation('word', '4')
        )
        self.assertTrue(
            self.solution.validWordAbbreviation('substitution', 's10n')
        )
        self.assertFalse(
            self.solution.validWordAbbreviation('word', '5')  # Too long
        )

    def test_multiple_consecutive_numbers(self):
        """Test handling of multiple digits in a number"""
        self.assertTrue(
            self.solution.validWordAbbreviation('internationalization', 'i18n')
        )
        self.assertTrue(
            self.solution.validWordAbbreviation('x' * 100, '100')
        )

    def test_mixed_letters_and_numbers(self):
        """Test complex patterns with alternating letters and numbers"""
        self.assertTrue(
            self.solution.validWordAbbreviation('accessibility', 'a11y')
        )
        self.assertTrue(
            self.solution.validWordAbbreviation('hello', 'h1l2')
        )
        self.assertFalse(
            self.solution.validWordAbbreviation('hello', 'h1l3')  # Goes past end
        )

    def test_edge_cases(self):
        """Test edge cases"""
        # Empty strings
        self.assertTrue(
            self.solution.validWordAbbreviation('', '')
        )
        # Single character
        self.assertTrue(
            self.solution.validWordAbbreviation('a', 'a')
        )
        self.assertTrue(
            self.solution.validWordAbbreviation('a', '1')
        )
        # Number at the end
        self.assertTrue(
            self.solution.validWordAbbreviation('word', 'wo2')
        )
        # Number at the beginning
        self.assertTrue(
            self.solution.validWordAbbreviation('word', '3d')
        )

    def test_invalid_patterns(self):
        """Test various invalid patterns"""
        # Abbreviation longer than word
        self.assertFalse(
            self.solution.validWordAbbreviation('hi', 'h3')
        )
        # Wrong character match
        self.assertFalse(
            self.solution.validWordAbbreviation('hello', 'h3p')
        )
        # Number extends past word length
        self.assertFalse(
            self.solution.validWordAbbreviation('hello', '10')
        )

    # CLAUDE-CODE END


if __name__ == '__main__':
    unittest.main()
