#!/usr/bin/env python3
"""
https://leetcode.com/problems/valid-word-abbreviation/

Author: Illya Starikov
Date: 2025-08-29
License: MIT
"""

import re


class Solution:
    def validWordAbbreviation(self, word: str, abbreviation: str) -> bool:
        return self.ValidWordAbbreviationRegex(word, abbreviation)

    def ValidWordAbbreviationIterative(self, word: str, abbreviation: str) -> bool:
        """
        Optimal two-pointer solution
        This is the most efficient approach for this problem.

        Time Complexity: O(n) where n = len(abbreviation)
        - Single pass through the abbreviation string
        - Each character is processed exactly once

        Space Complexity: O(1)
        - Only uses two integer pointers and one temporary number variable
        - No additional data structures created
        """
        word_idx, abbr_idx = 0, 0  # Pointers for word and abbreviation

        while word_idx < len(word) and abbr_idx < len(abbreviation):
            if abbreviation[abbr_idx].isdigit():
                # Leading zero check
                if abbreviation[abbr_idx] == '0':
                    return False

                # Parse the complete number
                num = 0
                while abbr_idx < len(abbreviation) and abbreviation[abbr_idx].isdigit():
                    num = num * 10 + int(abbreviation[abbr_idx])
                    abbr_idx += 1

                # Skip 'num' characters in word
                word_idx += num
            else:
                # Character must match
                if word[word_idx] != abbreviation[abbr_idx]:
                    return False
                word_idx += 1
                abbr_idx += 1

        # Both should be fully consumed
        return word_idx == len(word) and abbr_idx == len(abbreviation)

    def ValidWordAbbreviationRegex(self, word: str, abbreviation: str) -> bool:
        """
        Alternative regex solution - elegant but less efficient

        Time Complexity: O(n + m) where n = len(abbreviation), m = len(word)
        - O(n) to find all numbers with re.findall
        - O(n) to check for leading zeros
        - O(n) to build the pattern with re.sub
        - O(m) to match the pattern against the word

        Space Complexity: O(n + m)
        - O(k) for storing found numbers where k is count of numbers
        - O(n) for the generated regex pattern string
        - O(m) for regex engine's internal matching structures
        """
        # Check for leading zeros
        tokens = re.findall(r'\d+', abbreviation)
        if any(token[0] == '0' for token in tokens):
            return False

        # Convert abbreviation to regex pattern
        def replace_number(match):
            count = int(match.group(0))
            return f'.{{{count}}}'

        pattern = re.sub(r'\d+', replace_number, abbreviation)

        # Match the pattern against the word
        return re.fullmatch(pattern, word) is not None


# CLAUDE-CODE BEGIN
import unittest


class TestValidWordAbbreviation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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


if __name__ == '__main__':
    unittest.main()
# CLAUDE-CODE END
