#!/usr/bin/env python3
"""
26. Remove Duplicates from Sorted Array (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. Return k (the number of
unique elements), and modify the array so the first k elements contain unique
values in sorted order.

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - Array is sorted in non-decreasing order

Examples:
    Input: [1,1,2]
    Output: 2, nums = [1,2,_]

    Input: [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Edge Cases:
    - Single element: [1] -> 1
    - No duplicates: [1,2,3] -> 3
    - All duplicates: [1,1,1,1] -> 1
    - Two elements same: [1,1] -> 1
    - Two elements different: [1,2] -> 2
    - Negative numbers: [-3,-1,0,2] -> 4
    - Values at constraint boundaries: [-100, 100]
"""

# Pattern: Two-Pointer (Fast/Slow)
#     When to use:
#     - Sorted array problems
#     - In-place modifications required
#     - O(1) space constraint
#     - Finding pairs or removing elements
#
#     Telltale signs in this problem:
#     - "sorted in non-decreasing order"
#     - "remove duplicates in-place"
#     - "O(1) extra memory"
#
# Approach:
#     1. BRUTE FORCE: Use a set to track seen elements, copy uniques to new array
#        - Time: O(n), Space: O(n) - violates space constraint
#
#     2. OPTIMAL: Two pointers - one for reading, one for writing
#        - Insight: Since array is sorted, duplicates are adjacent
#        - Write pointer marks where next unique goes
#        - Read pointer scans for new values
#        - Time: O(n), Space: O(1)
#
# Clarifying Questions:
#     - Can I modify the input array? (Yes, in-place required)
#     - What to return for empty array? (Constraints say n >= 1)
#     - Are negative numbers possible? (Yes, -100 to 100)
#     - What about the elements after index k? (Don't matter)
#
# Common Mistakes:
#     - Starting both pointers at 0 (should start at 1 - first element always unique)
#     - Off-by-one in loop bounds
#     - Comparing to wrong element (compare to last written, not previous read)
#     - Using extra space (set/hashmap) when not needed
#
# Related Problems:
#     - 27. Remove Element (Easy) - similar two-pointer
#     - 80. Remove Duplicates II (Medium) - allow 2 duplicates
#     - 283. Move Zeroes (Easy) - similar in-place modification
#
# Follow-up Questions:
# 1. What if duplicates could appear at most twice? (LeetCode 80)
# 2. What if the array wasn't sorted?
# 3. For-loop vs while-loop - which is cleaner?

from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place using two-pointer technique.

        Args:
            nums: Sorted integer array (modified in-place).

        Returns:
            Number of unique elements k. First k elements contain unique values.

        Complexity:
            Time: O(n) - single pass through array
            Space: O(1) - only two pointers used
        """
        write_i = 1
        for read_i in range(1, len(nums)):
            if nums[read_i] != nums[write_i - 1]:
                nums[write_i] = nums[read_i]
                write_i += 1

        return write_i


class TestSolution(unittest.TestCase):
    """Tests for Remove Duplicates from Sorted Array solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Example 1: [1,1,2] -> k=2, nums[:k]=[1,2]."""
        nums = [1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_example_2(self):
        """Example 2: [0,0,1,1,1,2,2,3,3,4] -> k=5."""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_edge_single_element(self):
        """Single element array."""
        nums = [1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test_edge_no_duplicates(self):
        """Array with no duplicates."""
        nums = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

    def test_edge_all_same(self):
        """All elements identical."""
        nums = [1, 1, 1, 1, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test_edge_negative_numbers(self):
        """Negative numbers in array."""
        nums = [-3, -3, -1, 0, 0, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-3, -1, 0, 2])

    def test_edge_two_same(self):
        """Two identical elements."""
        nums = [1, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test_edge_two_different(self):
        """Two different elements."""
        nums = [1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_edge_constraint_boundaries(self):
        """Values at constraint boundaries."""
        nums = [-100, -100, 0, 100, 100]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [-100, 0, 100])


if __name__ == "__main__":
    unittest.main()
