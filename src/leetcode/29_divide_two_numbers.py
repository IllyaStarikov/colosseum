#!/usr/bin/env python3
"""LeetCode Problem 29: Divide Two Integers.

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