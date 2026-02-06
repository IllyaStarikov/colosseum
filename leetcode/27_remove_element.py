#!/usr/bin/env python3
"""
27. Remove Element (Easy)
https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Return the number
of elements in nums which are not equal to val.

After removing all occurrences of val, the first k elements of nums should
contain the elements which are not equal to val. It does not matter what is
left beyond the first k elements.

Constraints:
    - 0 <= nums.length <= 100
    - 0 <= nums[i] <= 50
    - 0 <= val <= 100

Examples:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]

    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]

Edge Cases:
    - Empty array: [] -> 0
    - No elements to remove: [1,2,3], val=4 -> 3
    - All elements should be removed: [3,3,3], val=3 -> 0
    - Single element (matches): [3], val=3 -> 0
    - Single element (doesn't match): [3], val=1 -> 1
    - Two elements same: [3,3], val=3 -> 0
    - Two elements different: [1,2], val=1 -> 1
"""

# Pattern: Two-Pointer (Fast/Slow)
#     When to use:
#     - Array modification in-place
#     - O(1) space constraint
#     - Removing or partitioning elements
#     - Order doesn't matter (can also be done when order matters)
#
#     Telltale signs in this problem:
#     - "remove all occurrences in-place"
#     - "order may be changed"
#     - "O(1) extra memory"
#
# Approach:
#     1. BRUTE FORCE: Create new array, copy non-val elements
#        - Time: O(n), Space: O(n) - violates space constraint
#
#     2. OPTIMAL: Two pointers - read pointer scans, write pointer marks position
#        - Insight: Only copy elements that don't match val
#        - Write pointer tracks where next valid element goes
#        - Read pointer scans through all elements
#        - Time: O(n), Space: O(1)
#
#     3. ALTERNATIVE: Two pointers from both ends (when val is rare)
#        - Swap element to remove with last element
#        - Useful when elements to remove are rare
#        - Time: O(n), Space: O(1)
#
# Clarifying Questions:
#     - Can I modify the input array? (Yes, in-place required)
#     - Does order matter? (No, order may be changed)
#     - What to return for empty array? (0)
#     - Can val appear multiple times? (Yes)
#     - Are there duplicates in nums? (Possible)
#
# Common Mistakes:
#     - Using extra space (new array) when not needed
#     - Forgetting to return the count k
#     - Off-by-one errors in loop bounds
#     - Modifying array while iterating incorrectly (pop approach is O(n^2))
#
# Related Problems:
#     - 26. Remove Duplicates from Sorted Array (Easy) - similar two-pointer
#     - 283. Move Zeroes (Easy) - similar in-place modification
#     - 80. Remove Duplicates from Sorted Array II (Medium) - allow 2 duplicates
#
# Follow-up Questions:
# 1. What if we needed to maintain the original order?
# 2. How would the solution change if val could appear in chunks?
# 3. What's the advantage of the swap-with-end approach?

from typing import List
import unittest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val from array in-place using two-pointer technique.

        Args:
            nums: Integer array (modified in-place).
            val: Value to remove from array.

        Returns:
            Number of elements k remaining. First k elements contain non-val values.

        Complexity:
            Time: O(n) - single pass through array
            Space: O(1) - only two pointers used
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     i = 0
    #     k = 0
    #
    #     while i < len(nums):
    #         if nums[i] == val:
    #             nums.pop(i)
    #         else:
    #             i += 1
    #             k += 1
    #
    #     return k


class TestSolution(unittest.TestCase):
    """Tests for Remove Element solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Example 1: [3,2,2,3], val=3 -> k=2."""
        nums = [3, 2, 2, 3]
        k = self.solution.removeElement(nums, 3)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_example_2(self):
        """Example 2: [0,1,2,2,3,0,4,2], val=2 -> k=5."""
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = self.solution.removeElement(nums, 2)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_edge_empty_array(self):
        """Empty array returns 0."""
        nums = []
        k = self.solution.removeElement(nums, 1)
        self.assertEqual(k, 0)

    def test_edge_no_elements_to_remove(self):
        """Value not in array."""
        nums = [1, 2, 3]
        k = self.solution.removeElement(nums, 4)
        self.assertEqual(k, 3)
        self.assertEqual(sorted(nums[:k]), [1, 2, 3])

    def test_edge_all_elements_removed(self):
        """All elements match val."""
        nums = [3, 3, 3]
        k = self.solution.removeElement(nums, 3)
        self.assertEqual(k, 0)

    def test_edge_single_element_matches(self):
        """Single element that matches."""
        nums = [3]
        k = self.solution.removeElement(nums, 3)
        self.assertEqual(k, 0)

    def test_edge_single_element_no_match(self):
        """Single element that doesn't match."""
        nums = [3]
        k = self.solution.removeElement(nums, 1)
        self.assertEqual(k, 1)
        self.assertEqual(nums[0], 3)

    def test_edge_two_same_both_removed(self):
        """Two identical elements, both removed."""
        nums = [3, 3]
        k = self.solution.removeElement(nums, 3)
        self.assertEqual(k, 0)

    def test_edge_two_different_one_removed(self):
        """Two different elements, one removed."""
        nums = [1, 2]
        k = self.solution.removeElement(nums, 1)
        self.assertEqual(k, 1)
        self.assertEqual(nums[0], 2)


if __name__ == "__main__":
    unittest.main()
