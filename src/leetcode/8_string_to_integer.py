#!/usr/bin/env python3
"""LeetCode Problem 8: String to Integer (atoi).

Implements the atoi function which converts a string to an integer.

Author: Illya Starikov
Date: 08/03/19
License: MIT
"""

import re
from typing import Optional

INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


class Solution:
    """Solution for the String to Integer problem."""
    
    @staticmethod
    def _in_range(number: int) -> bool:
        """Check if number is within 32-bit signed integer range.
        
        Args:
            number: Integer to check.
            
        Returns:
            True if number is within range, False otherwise.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return INT_MIN <= number <= INT_MAX
    
    @staticmethod
    def _find_number(string: str) -> int:
        """Extract integer from string following atoi rules.
        
        Args:
            string: Input string to parse.
            
        Returns:
            Extracted integer or 0 if no valid number found.
            
        Time Complexity: O(n) where n is the length of string
        Space Complexity: O(1) for regex pattern matching
        """
        START = '^'
        WHITESPACE = ' '
        DIGIT = r'\d'
        PLUS_MINUS = r'[\+\-]'
        ANY = '.'
        
        regex_string = f"{START}{WHITESPACE}*({PLUS_MINUS}?)({DIGIT}+){ANY}*"
        
        regex = re.compile(regex_string)
        result = regex.match(string)
        
        try:
            plus_minus = result[1]
            numbers = result[2]
            
            if plus_minus in ['+', '']:
                return int(numbers)
            else:
                return -int(numbers)
        except (AttributeError, TypeError):
            return 0
    
    def myAtoi(self, string: str) -> int:
        """Convert string to 32-bit signed integer (atoi).
        
        Args:
            string: Input string to convert.
            
        Returns:
            Converted integer, clamped to 32-bit signed range.
            
        Time Complexity: O(n) where n is the length of string
        Space Complexity: O(1)
        """
        number = Solution._find_number(string)
        
        if not Solution._in_range(number):
            return INT_MIN if number < 0 else INT_MAX
        else:
            return number


import unittest


class TestStringToInteger(unittest.TestCase):
    """Test cases for String to Integer solution."""

    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()

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