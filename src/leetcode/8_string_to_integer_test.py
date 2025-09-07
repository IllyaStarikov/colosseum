#!/usr/bin/env python3
"""Tests for LeetCode Problem 8: String to Integer (atoi).

Author: Illya Starikov
Date: 08/03/19
License: MIT
"""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
solution_module = __import__("8_string_to_integer")


class TestStringToInteger(unittest.TestCase):
    """Test cases for String to Integer solution."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = solution_module.Solution()
    
    def test_negative_overflow(self):
        """Test negative number that overflows."""
        self.assertEqual(self.solution.myAtoi("-91283472332"), -2147483648)
    
    def test_basic_positive(self):
        """Test basic positive number."""
        self.assertEqual(self.solution.myAtoi("42"), 42)
    
    def test_with_whitespace(self):
        """Test number with leading whitespace."""
        self.assertEqual(self.solution.myAtoi("   -42"), -42)
    
    def test_with_words(self):
        """Test number followed by words."""
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)
    
    def test_words_before_number(self):
        """Test words before number (invalid)."""
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)
    
    def test_positive_overflow(self):
        """Test positive overflow."""
        self.assertEqual(self.solution.myAtoi("2147483648"), 2147483647)
    
    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(self.solution.myAtoi(""), 0)
    
    def test_plus_sign(self):
        """Test explicit plus sign."""
        self.assertEqual(self.solution.myAtoi("+1"), 1)
    
    def test_leading_zero(self):
        """Test number with leading zeros."""
        self.assertEqual(self.solution.myAtoi("0012"), 12)


if __name__ == '__main__':
    unittest.main()