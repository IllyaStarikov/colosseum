#!/usr/local/bin/python3
#
# 8-string-to-integer.py
# leetcode
#
# Created by Illya Starikov on 08/03/19.
# Copyright 2019. Illya Starikov. MIT License.

import re

INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


class Solution:
    @staticmethod
    def __in_range(number):
        return INT_MIN <= number <= INT_MAX

    @staticmethod
    def __find_number(string):
        START = '^'
        WHITESPACE = ' '
        DIGIT = '\d'
        PLUS_MINUS = '[\+\-]'
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
        except:
            return 0

    def myAtoi(self, string: str) -> int:
        number = Solution.__find_number(string)

        if not Solution.__in_range(number):
            return INT_MIN if number < 0 else INT_MAX
        else:
            return number

solution = Solution()
print(solution.myAtoi("-91283472332"))
