#!/usr/bin/env python3
"""29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/

Divide two integers without using multiplication, division, and mod operator.

Author: Illya Starikov
Date: 08/04/19
License: MIT
"""

INT_MIN = -(2 ** 31)
INT_MAX = 2**31 - 1


class Solution:
    """Solution for the Divide Two Integers problem."""
    
    def divide(self, dividend: int, divisor: int) -> int:
        """Divide two integers without using *, /, or % operators.
        
        Args:
            dividend: Number to be divided.
            divisor: Number to divide by.
            
        Returns:
            Integer quotient, clamped to 32-bit signed range.
            
        Time Complexity: O(dividend/divisor) - linear in the quotient value
        Space Complexity: O(1)
        
        Note: This is a naive implementation. A more efficient approach
        would use bit shifting for O(log n) complexity.
        """
        result = 0
        sign_mismatch = dividend * divisor < 0
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            dividend -= divisor
            result += 1
        
        result = -result if sign_mismatch else result
        result = Solution._check_bounds(result)
        
        return result
    
    @staticmethod
    def _check_bounds(number: int) -> int:
        """Clamp number to 32-bit signed integer range.

        Args:
            number: Integer to check.

        Returns:
            Number clamped to [INT_MIN, INT_MAX] range.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return INT_MAX if not (INT_MIN <= number <= INT_MAX) else number


import unittest


class TestDivideTwoNumbers(unittest.TestCase):
    """Test cases for Divide Two Integers solution."""

    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()

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