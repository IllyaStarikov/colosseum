#!/usr/local/bin/python3
#
# 29-divide-two-numbers.py
# leetcode
#
# Created by Illya Starikov on 08/04/19.
# Copyright 2019. Illya Starikov. MIT License.
#

INT_MIN, INT_MAX = -(2 ** 31),  2**31 - 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign_mismatch = dividend * divisor < 0

        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            dividend -= divisor
            result += 1

        result = -result if sign_mismatch else result
        result = Solution.__check_bounds(result)

        return result

    @staticmethod
    def __check_bounds(number):
        return INT_MAX if not (INT_MIN <= number <= INT_MAX) else number
