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


