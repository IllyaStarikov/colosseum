#!/usr/bin/env python3
"""
8. String to Integer (atoi) (Medium)
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit
signed integer.

The algorithm for myAtoi(string s) is as follows:
1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or
   '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit
   character is encountered or the end of the string is reached. If no digits
   were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range
   [-2^31, 2^31 - 1], round the integer to remain in the range.

Return the integer as the final result.

Constraints:
    - 0 <= s.length <= 200
    - s consists of English letters (lower-case and upper-case), digits (0-9),
      ' ', '+', '-', and '.'

Examples:
    Input: s = "42"
    Output: 42

    Input: s = "   -042"
    Output: -42
    Explanation: Leading whitespace ignored, '-' makes it negative,
    leading zeros ignored.

    Input: s = "1337c0d3"
    Output: 1337
    Explanation: Reading stops at 'c' (non-digit).

    Input: s = "0-1"
    Output: 0
    Explanation: Reading stops at '-' (non-digit after digit).

    Input: s = "words and 987"
    Output: 0
    Explanation: Reading stops at 'w' (first character is non-digit).

Edge Cases:
    - Empty string: "" -> 0
    - Only whitespace: "   " -> 0
    - Only sign: "+" or "-" -> 0
    - Leading zeros: "0012" -> 12
    - Positive overflow: "2147483648" -> 2147483647
    - Negative overflow: "-91283472332" -> -2147483648
    - Mixed with letters: "4193 with words" -> 4193
    - Letters before number: "words and 987" -> 0
    - Explicit plus sign: "+1" -> 1
    - Decimal point: "3.14159" -> 3
"""

# Pattern: String Parsing / State Machine
#     When to use:
#     - Parsing structured text
#     - Converting string to numeric types
#     - Handling multiple parsing rules sequentially
#     - Input validation with specific format rules
#
#     Telltale signs in this problem:
#     - Sequential parsing rules (whitespace, sign, digits)
#     - "ignore leading whitespace"
#     - "stop at non-digit character"
#     - Integer overflow handling
#
# Approach:
#     1. REGEX: Use regular expression to match pattern
#        - Pattern: ^\\s*([+-]?)(\\d+)
#        - Time: O(n), Space: O(n) for regex engine
#
#     2. ITERATIVE: Process character by character
#        - Skip whitespace, check sign, accumulate digits
#        - Stop on first non-digit after starting digit parsing
#        - Time: O(n), Space: O(1)
#
#     Both approaches are valid; regex is more concise but iterative
#     is often preferred in interviews to demonstrate understanding.
#
# Clarifying Questions:
#     - What about decimal points? (Treat as non-digit, stop parsing)
#     - Multiple signs like "--42"? (Invalid, return 0)
#     - Scientific notation "1e10"? (Stop at 'e', return 1)
#     - Unicode digits? (Only ASCII digits 0-9)
#     - Empty string? (Return 0)
#
# Common Mistakes:
#     - Not handling leading whitespace
#     - Forgetting the explicit '+' sign case
#     - Integer overflow during accumulation (check before multiplying)
#     - Not stopping at first non-digit after digits start
#     - Using int() without bounds checking
#
# Related Problems:
#     - 7. Reverse Integer (Medium) - similar overflow handling
#     - 65. Valid Number (Hard) - more complex number parsing
#     - 67. Add Binary (Easy) - string to number operations
#
# Follow-up Questions:
# 1. How would you handle locale-specific number formats?
# 2. What if we needed to parse floating-point numbers?
# 3. How would you implement this without regex?

import re

INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


class Solution:
    @staticmethod
    def _in_range(number: int) -> bool:
        """
        Check if number is within 32-bit signed integer range.

        Args:
            number: Integer to check.

        Returns:
            True if number is within range, False otherwise.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return INT_MIN <= number <= INT_MAX

    @staticmethod
    def _find_number(string: str) -> int:
        """
        Extract integer from string following atoi rules.

        Args:
            string: Input string to parse.

        Returns:
            Extracted integer or 0 if no valid number found.

        Complexity:
            Time: O(n) where n is the length of string
            Space: O(1) for regex pattern matching
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
        """
        Convert string to 32-bit signed integer (atoi).

        Uses regex to extract optional sign and digits from the string,
        following standard atoi parsing rules.

        Args:
            string: Input string to convert.

        Returns:
            Converted integer, clamped to 32-bit signed range.

        Complexity:
            Time: O(n) where n is the length of string
            Space: O(1)
        """
        number = Solution._find_number(string)

        if not Solution._in_range(number):
            return INT_MIN if number < 0 else INT_MAX
        else:
            return number


if __name__ == "__main__":
    s = Solution()

    # Example 1: Basic positive
    assert s.myAtoi("42") == 42, "Basic positive failed"

    # Example 2: Leading whitespace and sign
    assert s.myAtoi("   -42") == -42, "Whitespace and sign failed"

    # Example 3: Number with words after
    assert s.myAtoi("4193 with words") == 4193, "Number with words failed"

    # Example 4: Words before number
    assert s.myAtoi("words and 987") == 0, "Words before number failed"

    # Negative overflow
    assert s.myAtoi("-91283472332") == -2147483648, "Negative overflow failed"

    # Positive overflow
    assert s.myAtoi("2147483648") == 2147483647, "Positive overflow failed"

    # Empty string
    assert s.myAtoi("") == 0, "Empty string failed"

    # Plus sign
    assert s.myAtoi("+1") == 1, "Plus sign failed"

    # Leading zero
    assert s.myAtoi("0012") == 12, "Leading zero failed"

    # Only whitespace
    assert s.myAtoi("   ") == 0, "Only whitespace failed"

    # Sign without number
    assert s.myAtoi("-") == 0, "Sign without number failed"

    # Zero
    assert s.myAtoi("0") == 0, "Zero failed"

    # Decimal point stops parsing
    assert s.myAtoi("3.14159") == 3, "Decimal point failed"

    # Number then sign then number
    assert s.myAtoi("0-1") == 0, "Number then sign failed"

    print("All tests passed!")
