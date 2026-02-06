#!/usr/bin/env python3
"""
408. Valid Word Abbreviation (Easy)
https://leetcode.com/problems/valid-word-abbreviation/

A string can be abbreviated by replacing any number of non-adjacent, non-empty
substrings with their lengths. The lengths should not have leading zeros.

For example, "substitution" could be abbreviated as:
- "s10n" ("s ubstitutio n")
- "sub4u4" ("sub stit u tion")
- "12" ("substitution")
- "su3i1u2on" ("su bst i t u ti on")

The following are NOT valid abbreviations:
- "s55n" (replaced substrings are adjacent)
- "s010n" (has leading zeros)
- "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches
the given abbreviation.

Constraints:
    - 1 <= word.length <= 20
    - word consists of only lowercase English letters
    - 1 <= abbr.length <= 10
    - abbr consists of lowercase English letters and digits
    - All integers in abbr will fit in a 32-bit integer

Examples:
    Input: word = "internationalization", abbr = "i12iz4n"
    Output: true
    Explanation: "i nternational iz atio n"

    Input: word = "apple", abbr = "a2e"
    Output: false

Edge Cases:
    - Exact match no numbers: "apple", "apple" -> true
    - Full abbreviation: "word", "4" -> true
    - Leading zero invalid: "apple", "a03e" -> false
    - "0" replacement invalid: "word", "w01d" -> false
    - Number extends past word: "hello", "h3p" -> false
    - Number at end: "word", "wo2" -> true
    - Number at beginning: "word", "3d" -> true
    - Empty strings: "", "" -> true
    - Single character: "a", "a" -> true, "a", "1" -> true
    - Number too large: "hello", "10" -> false
"""

# Pattern: Two-Pointer String Matching
#     When to use:
#     - Comparing two strings with transformations
#     - Parsing strings with mixed character types
#     - Sequential validation of string patterns
#
#     Telltale signs in this problem:
#     - "matches the given abbreviation"
#     - Mixed letters and numbers in pattern
#     - Need to track position in both strings
#
# Approach:
#     1. BRUTE FORCE: Generate all possible expansions of abbreviation
#        - Time: O(2^n) exponential, Space: O(n)
#
#     2. OPTIMAL: Two-pointer simulation
#        - One pointer for word, one for abbreviation
#        - If letter in abbr, must match word letter
#        - If digit in abbr, parse full number and skip that many chars in word
#        - Check for leading zeros (invalid)
#        - Time: O(n + m), Space: O(1)
#
#     3. ALTERNATIVE: Regex-based solution
#        - Convert abbreviation to regex pattern
#        - Match against word
#        - Time: O(n + m), Space: O(n) for pattern
#
# Clarifying Questions:
#     - Can abbreviation have leading zeros in numbers? (No, invalid)
#     - Can "0" be used as a number? (No, can't replace empty substring)
#     - Case sensitive? (Yes, lowercase only per constraints)
#     - Can abbreviation be longer than word? (Yes, if numbers skip enough)
#     - Empty inputs? (Both empty is valid)
#
# Common Mistakes:
#     - Not checking for leading zeros in numbers
#     - Not handling multi-digit numbers correctly
#     - Forgetting to check if both pointers reach end
#     - Off-by-one when skipping characters
#     - Using "0" as a valid number (it's not)
#
# Related Problems:
#     - 527. Word Abbreviation (Hard) - generate unique abbreviations
#     - 411. Minimum Unique Word Abbreviation (Hard) - shortest valid abbreviation
#     - 288. Unique Word Abbreviation (Medium) - abbreviation dictionary
#
# Follow-up Questions:
# 1. How would you generate all valid abbreviations for a word?
# 2. What if we needed to find the shortest valid abbreviation?
# 3. How would you handle case-insensitive matching?

import re
import unittest


class Solution:
    def validWordAbbreviation(self, word: str, abbreviation: str) -> bool:
        """
        Check if abbreviation matches word.

        Args:
            word: Original word to match.
            abbreviation: Abbreviated form to validate.

        Returns:
            True if abbreviation is valid for word, False otherwise.

        Complexity:
            Time: O(n + m) where n = len(word), m = len(abbreviation)
            Space: O(1) - only pointers used
        """
        return self.ValidWordAbbreviationIterative(word, abbreviation)

    def ValidWordAbbreviationIterative(self, word: str, abbreviation: str) -> bool:
        """
        Optimal two-pointer solution.

        Args:
            word: Original word to match.
            abbreviation: Abbreviated form to validate.

        Returns:
            True if abbreviation is valid for word, False otherwise.

        Complexity:
            Time: O(n) where n = len(abbreviation) - single pass
            Space: O(1) - only two integer pointers
        """
        word_idx, abbr_idx = 0, 0

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
        Alternative regex solution - elegant but less efficient.

        Args:
            word: Original word to match.
            abbreviation: Abbreviated form to validate.

        Returns:
            True if abbreviation is valid for word, False otherwise.

        Complexity:
            Time: O(n + m) where n = len(abbreviation), m = len(word)
            Space: O(n + m) for pattern and regex structures
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


class TestSolution(unittest.TestCase):
    """Tests for Valid Word Abbreviation solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_valid_multiple_numbers(self):
        """Example 1: Valid abbreviation with multiple numbers."""
        self.assertTrue(self.solution.validWordAbbreviation('internationalization', 'i12iz4n'))

    def test_example_invalid(self):
        """Example 2: Invalid abbreviation."""
        self.assertFalse(self.solution.validWordAbbreviation('apple', 'a2e'))

    def test_edge_leading_zero(self):
        """Leading zero is invalid."""
        self.assertFalse(self.solution.validWordAbbreviation('apple', 'a03e'))

    def test_edge_leading_zero_middle(self):
        """Leading zero in middle is invalid."""
        self.assertFalse(self.solution.validWordAbbreviation('word', 'w01d'))

    def test_edge_exact_match(self):
        """Exact match without numbers."""
        self.assertTrue(self.solution.validWordAbbreviation('apple', 'apple'))

    def test_edge_wrong_letter(self):
        """Wrong letter invalidates."""
        self.assertFalse(self.solution.validWordAbbreviation('apple', 'appla'))

    def test_edge_full_number(self):
        """Entire word as number."""
        self.assertTrue(self.solution.validWordAbbreviation('word', '4'))

    def test_edge_s10n(self):
        """Classic abbreviation pattern."""
        self.assertTrue(self.solution.validWordAbbreviation('substitution', 's10n'))

    def test_edge_number_too_large(self):
        """Number larger than word length."""
        self.assertFalse(self.solution.validWordAbbreviation('word', '5'))

    def test_edge_i18n(self):
        """i18n pattern."""
        self.assertTrue(self.solution.validWordAbbreviation('internationalization', 'i18n'))

    def test_edge_100_chars(self):
        """100 character word."""
        self.assertTrue(self.solution.validWordAbbreviation('x' * 100, '100'))

    def test_edge_a11y(self):
        """a11y pattern."""
        self.assertTrue(self.solution.validWordAbbreviation('accessibility', 'a11y'))

    def test_edge_h1l2(self):
        """Mixed letters and numbers."""
        self.assertTrue(self.solution.validWordAbbreviation('hello', 'h1l2'))

    def test_edge_h1l3_extends_past(self):
        """Number extends past word end."""
        self.assertFalse(self.solution.validWordAbbreviation('hello', 'h1l3'))

    def test_edge_empty_strings(self):
        """Both empty strings match."""
        self.assertTrue(self.solution.validWordAbbreviation('', ''))

    def test_edge_single_char_match(self):
        """Single character match."""
        self.assertTrue(self.solution.validWordAbbreviation('a', 'a'))

    def test_edge_single_char_number(self):
        """Single character as number."""
        self.assertTrue(self.solution.validWordAbbreviation('a', '1'))

    def test_edge_number_at_end(self):
        """Number at end of abbreviation."""
        self.assertTrue(self.solution.validWordAbbreviation('word', 'wo2'))

    def test_edge_number_at_beginning(self):
        """Number at beginning of abbreviation."""
        self.assertTrue(self.solution.validWordAbbreviation('word', '3d'))

    def test_edge_abbreviation_longer(self):
        """Abbreviation longer than possible."""
        self.assertFalse(self.solution.validWordAbbreviation('hi', 'h3'))

    def test_edge_wrong_char_after_number(self):
        """Wrong character after number."""
        self.assertFalse(self.solution.validWordAbbreviation('hello', 'h3p'))

    def test_edge_number_exceeds_length(self):
        """Number exceeds word length."""
        self.assertFalse(self.solution.validWordAbbreviation('hello', '10'))


if __name__ == "__main__":
    unittest.main()
