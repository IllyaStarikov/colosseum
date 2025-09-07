#!/usr/bin/env python3
"""Tests for LeetCode Problem 29: Divide Two Integers.

Author: Illya Starikov
Date: 08/04/19
License: MIT
"""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
solution_module = __import__("29_divide_two_numbers")


class TestDivideTwoNumbers(unittest.TestCase):
    """Test cases for Divide Two Integers solution."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = solution_module.Solution()
    
    def test_basic_division(self):
        """Test basic division."""
        self.assertEqual(self.solution.divide(10, 3), 3)
    
    def test_negative_division(self):
        """Test division with negative numbers."""
        self.assertEqual(self.solution.divide(7, -3), -2)
    
    def test_both_negative(self):
        """Test division with both numbers negative."""
        self.assertEqual(self.solution.divide(-7, -3), 2)
    
    def test_zero_dividend(self):
        """Test zero dividend."""
        self.assertEqual(self.solution.divide(0, 1), 0)
    
    def test_divide_by_one(self):
        """Test division by one."""
        self.assertEqual(self.solution.divide(5, 1), 5)
    
    def test_divide_by_negative_one(self):
        """Test division by negative one."""
        self.assertEqual(self.solution.divide(5, -1), -5)
    
    def test_overflow_case(self):
        """Test overflow case: INT_MIN / -1."""
        self.assertEqual(
            self.solution.divide(-2147483648, -1), 
            2147483647
        )
    
    def test_large_numbers(self):
        """Test with large numbers."""
        self.assertEqual(self.solution.divide(100000, 1), 100000)


if __name__ == '__main__':
    unittest.main()