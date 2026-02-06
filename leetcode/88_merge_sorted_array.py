#!/usr/bin/env python3
"""
88. Merge Sorted Array (Easy)
https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order. The
final sorted array should not be returned by the function, but instead be stored
inside the array nums1.

To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set to 0
and should be ignored. nums2 has a length of n.

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9

Examples:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]

Edge Cases:
    - nums2 is empty: [1], m=1, [], n=0 -> [1]
    - nums1 has no initial elements: [0], m=0, [1], n=1 -> [1]
    - All nums2 elements smaller: [4,5,6,0,0,0], m=3, [1,2,3], n=3 -> [1,2,3,4,5,6]
    - All nums2 elements larger: [1,2,3,0,0,0], m=3, [4,5,6], n=3 -> [1,2,3,4,5,6]
    - Interleaved elements: [1,3,5,0,0,0], m=3, [2,4,6], n=3 -> [1,2,3,4,5,6]
    - Duplicate values: [1,2,2,0,0], m=3, [2,3], n=2 -> [1,2,2,2,3]
    - Negative numbers: [-3,-1,0,0,0], m=2, [-2,1,2], n=3 -> [-3,-2,-1,1,2]
"""

# Pattern: Three-Pointer (Merge from End)
#     When to use:
#     - Merging sorted arrays in-place
#     - One array has extra space at the end
#     - O(1) space constraint
#     - Need to avoid overwriting unprocessed elements
#
#     Telltale signs in this problem:
#     - "two sorted arrays"
#     - "merge in-place"
#     - "nums1 has a length of m + n"
#
# Approach:
#     1. BRUTE FORCE: Copy nums2 to end of nums1, then sort
#        - Time: O((m+n) log(m+n)), Space: O(1)
#
#     2. SUBOPTIMAL: Use extra array to merge, copy back
#        - Time: O(m+n), Space: O(m+n) - violates space constraint
#
#     3. OPTIMAL: Three pointers, fill from the back
#        - Insight: Fill from end to avoid overwriting nums1 elements
#        - p1 points to last element of nums1 (index m-1)
#        - p2 points to last element of nums2 (index n-1)
#        - write points to last position of nums1 (index m+n-1)
#        - Compare and place larger element at write position
#        - Time: O(m+n), Space: O(1)
#
# Clarifying Questions:
#     - Can I modify nums1 in-place? (Yes, required)
#     - Is nums1 guaranteed to have enough space? (Yes, length is m+n)
#     - What if one array is empty? (Handle gracefully)
#     - Are arrays guaranteed to be sorted? (Yes, non-decreasing order)
#     - Can there be duplicates? (Yes)
#
# Common Mistakes:
#     - Merging from the front (overwrites unprocessed nums1 elements)
#     - Forgetting to handle when one array is exhausted
#     - Off-by-one errors with pointer initialization
#     - Not handling the case when nums1 is empty (m=0)
#
# Related Problems:
#     - 21. Merge Two Sorted Lists (Easy) - linked list version
#     - 977. Squares of a Sorted Array (Easy) - similar two-pointer merge
#     - 23. Merge k Sorted Lists (Hard) - generalization to k arrays
#
# Follow-up Questions:
# 1. What if both arrays were unsorted?
# 2. Can you do this with a single while loop?
# 3. What if nums1 didn't have extra space at the end?

from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place using three-pointer technique.

        Uses a three-pointer approach, filling from the back to avoid
        overwriting elements in nums1 that haven't been processed yet.

        Args:
            nums1: First sorted array with m elements followed by n zeros.
            m: Number of actual elements in nums1.
            nums2: Second sorted array with n elements.
            n: Number of elements in nums2.

        Complexity:
            Time: O(m + n) - each element processed once
            Space: O(1) - only three pointers used
        """
        p1, p2, write_idx = m - 1, n - 1, m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write_idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[write_idx] = nums2[p2]
                p2 -= 1
            write_idx -= 1


class TestSolution(unittest.TestCase):
    """Tests for Merge Sorted Array solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Example 1: Basic merge."""
        nums1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(nums1, 3, [2, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example_2(self):
        """Example 2: nums2 is empty."""
        nums1 = [1]
        self.solution.merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        """Example 3: nums1 has no initial elements."""
        nums1 = [0]
        self.solution.merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

    def test_edge_all_smaller(self):
        """All nums2 elements smaller than nums1."""
        nums1 = [4, 5, 6, 0, 0, 0]
        self.solution.merge(nums1, 3, [1, 2, 3], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_edge_all_larger(self):
        """All nums2 elements larger than nums1."""
        nums1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(nums1, 3, [4, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_edge_interleaved(self):
        """Elements interleave."""
        nums1 = [1, 3, 5, 0, 0, 0]
        self.solution.merge(nums1, 3, [2, 4, 6], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_edge_duplicates(self):
        """Duplicate values across arrays."""
        nums1 = [1, 2, 2, 0, 0]
        self.solution.merge(nums1, 3, [2, 3], 2)
        self.assertEqual(nums1, [1, 2, 2, 2, 3])

    def test_edge_negative_numbers(self):
        """Negative numbers in arrays."""
        nums1 = [-3, -1, 0, 0, 0]
        self.solution.merge(nums1, 2, [-2, 1, 2], 3)
        self.assertEqual(nums1, [-3, -2, -1, 1, 2])


if __name__ == "__main__":
    unittest.main()
