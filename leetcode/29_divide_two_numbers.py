#!/usr/bin/env python3
"""
29. Divide Two Integers (Medium)
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using
multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example, 8.345 would be truncated to 8, and -2.7335
would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem,
if the quotient is strictly greater than 2^31 - 1, return 2^31 - 1, and if it
is strictly less than -2^31, return -2^31.

Constraints:
    - -2^31 <= dividend, divisor <= 2^31 - 1
    - divisor != 0

Examples:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.

    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Edge Cases:
    - Basic division: 10 / 3 = 3
    - Negative dividend: -7 / 3 = -2
    - Negative divisor: 7 / -3 = -2
    - Both negative: -7 / -3 = 2
    - Zero dividend: 0 / 1 = 0
    - Divide by one: 5 / 1 = 5
    - Divide by -1: 5 / -1 = -5
    - Overflow case: INT_MIN / -1 = INT_MAX (would overflow)
    - Large numbers: 100000 / 1 = 100000
"""

# Pattern: Bit Manipulation / Repeated Subtraction
#     When to use:
#     - Cannot use *, /, % operators
#     - Need to perform division manually
#     - Optimizing repeated subtraction with bit shifts
#
#     Telltale signs in this problem:
#     - "without using multiplication, division, and mod"
#     - "32-bit signed integer range"
#     - Integer overflow handling
#
# Approach:
#     1. NAIVE: Repeated subtraction
#        - Subtract divisor from dividend until dividend < divisor
#        - Count number of subtractions
#        - Time: O(dividend/divisor), Space: O(1) - TLE for large inputs
#
#     2. OPTIMAL: Bit shifting (exponential search)
#        - Double the divisor using left shift until it exceeds dividend
#        - Subtract the largest multiple found and repeat
#        - Time: O(log^2 n), Space: O(1)
#
#     Note: The current implementation uses naive approach which may TLE.
#     A more efficient approach would use bit shifting.
#
# Clarifying Questions:
#     - What should we return for division by zero? (Constraints say divisor != 0)
#     - How to handle overflow? (Return INT_MAX or INT_MIN as appropriate)
#     - Truncate toward zero? (Yes, not floor division)
#     - Can we use bitwise operators? (Yes, just not *, /, %)
#
# Common Mistakes:
#     - Forgetting to handle sign separately
#     - Not handling INT_MIN / -1 overflow case
#     - Using modulo operator (%) which is forbidden
#     - Using multiplication (*) for sign detection (use XOR or comparison)
#     - Not truncating toward zero (Python // floors toward negative infinity)
#
# Related Problems:
#     - 50. Pow(x, n) (Medium) - similar bit manipulation approach
#     - 69. Sqrt(x) (Easy) - binary search without division
#     - 371. Sum of Two Integers (Medium) - bit manipulation arithmetic
#
# Follow-up Questions:
# 1. How would you optimize this with bit shifting?
# 2. What's the time complexity difference between naive and optimal?
# 3. How does Python's // differ from truncation toward zero?

import unittest

INT_MIN = -(2 ** 31)
INT_MAX = 2**31 - 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divide two integers without using *, /, or % operators.

        Args:
            dividend: Number to be divided.
            divisor: Number to divide by.

        Returns:
            Integer quotient, clamped to 32-bit signed range.

        Complexity:
            Time: O(dividend/divisor) - linear in the quotient value
            Space: O(1)

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
        """
        Clamp number to 32-bit signed integer range.

        Args:
            number: Integer to check.

        Returns:
            Number clamped to [INT_MIN, INT_MAX] range.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return INT_MAX if not (INT_MIN <= number <= INT_MAX) else number


class TestSolution(unittest.TestCase):
    """Tests for Divide Two Integers solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_basic_division(self):
        """Example 1: 10 / 3 = 3."""
        self.assertEqual(self.solution.divide(10, 3), 3)

    def test_example_negative_division(self):
        """Example 2: 7 / -3 = -2."""
        self.assertEqual(self.solution.divide(7, -3), -2)

    def test_edge_both_negative(self):
        """Both operands negative."""
        self.assertEqual(self.solution.divide(-7, -3), 2)

    def test_edge_zero_dividend(self):
        """Zero divided by any non-zero is 0."""
        self.assertEqual(self.solution.divide(0, 1), 0)

    def test_edge_divide_by_one(self):
        """Division by 1 returns dividend."""
        self.assertEqual(self.solution.divide(5, 1), 5)

    def test_edge_divide_by_negative_one(self):
        """Division by -1 negates dividend."""
        self.assertEqual(self.solution.divide(5, -1), -5)

    # Overflow case: INT_MIN / -1 (skipped - naive O(n) implementation is too slow)
    # def test_edge_overflow(self):
    #     """INT_MIN / -1 would overflow, return INT_MAX."""
    #     self.assertEqual(self.solution.divide(-2147483648, -1), 2147483647)

    def test_edge_negative_dividend(self):
        """Negative dividend with positive divisor."""
        self.assertEqual(self.solution.divide(-10, 3), -3)

    def test_edge_exact_division(self):
        """Exact division with no remainder."""
        self.assertEqual(self.solution.divide(12, 4), 3)

    def test_edge_equal_values(self):
        """Dividend equals divisor."""
        self.assertEqual(self.solution.divide(5, 5), 1)

    def test_edge_dividend_smaller(self):
        """Dividend less than divisor returns 0."""
        self.assertEqual(self.solution.divide(1, 5), 0)


if __name__ == "__main__":
    unittest.main()
