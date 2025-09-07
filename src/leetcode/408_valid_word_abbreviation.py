#!/usr/bin/env python3
"""
https://leetcode.com/problems/valid-word-abbreviation/

Author: Illya Starikov
Date: 2025-08-29
License: MIT
"""

import re


class Solution:
    def validWordAbbreviation(self, word: str, abbreviation: str) -> bool:
        return self.ValidWordAbbreviationRegex(word, abbreviation)

    def ValidWordAbbreviationIterative(self, word: str, abbreviation: str) -> bool:
        """
        Optimal two-pointer solution
        This is the most efficient approach for this problem.

        Time Complexity: O(n) where n = len(abbreviation)
        - Single pass through the abbreviation string
        - Each character is processed exactly once

        Space Complexity: O(1)
        - Only uses two integer pointers and one temporary number variable
        - No additional data structures created
        """
        word_idx, abbr_idx = 0, 0  # Pointers for word and abbreviation

        while word_idx < len(word) and abbr_idx < len(abbreviation):
            if abbreviation[abbr_idx].isdigit():
                # Leading zero check
                if abbreviation[abbr_idx] == '0':
                    return False

                # Parse the complete number
                num = 0
                while abbr_idx < len(abbreviation) and abbreviation[abbr_idx].isdigit():
                    num = num * 10 + int(abbreviation[abbr_idx])
                    abbr_idx += 1

                # Skip 'num' characters in word
                word_idx += num
            else:
                # Character must match
                if word[word_idx] != abbreviation[abbr_idx]:
                    return False
                word_idx += 1
                abbr_idx += 1

        # Both should be fully consumed
        return word_idx == len(word) and abbr_idx == len(abbreviation)

    def ValidWordAbbreviationRegex(self, word: str, abbreviation: str) -> bool:
        """
        Alternative regex solution - elegant but less efficient

        Time Complexity: O(n + m) where n = len(abbreviation), m = len(word)
        - O(n) to find all numbers with re.findall
        - O(n) to check for leading zeros
        - O(n) to build the pattern with re.sub
        - O(m) to match the pattern against the word

        Space Complexity: O(n + m)
        - O(k) for storing found numbers where k is count of numbers
        - O(n) for the generated regex pattern string
        - O(m) for regex engine's internal matching structures
        """
        # Check for leading zeros
        tokens = re.findall(r'\d+', abbreviation)
        if any(token[0] == '0' for token in tokens):
            return False

        # Convert abbreviation to regex pattern
        def replace_number(match):
            count = int(match.group(0))
            return f'.{{{count}}}'

        pattern = re.sub(r'\d+', replace_number, abbreviation)

        # Match the pattern against the word
        return re.fullmatch(pattern, word) is not None

