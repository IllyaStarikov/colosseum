#!/usr/bin/env python3
"""
https://leetcode.com/problems/valid-word-abbreviation/

Author: Illya Starikov
Date: 2025-08-29
License: MIT
"""

import unittest
import sys
import pathlib

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


if __name__ == '__main__':
    unittest.main()
