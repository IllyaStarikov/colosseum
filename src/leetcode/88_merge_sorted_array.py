#!/usr/bin/env python3
"""88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array in-place. nums1 has enough space (size m + n) to hold elements
from both arrays.

Author: Illya Starikov
Date: 2026-01-28
License: MIT
"""

import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merge nums2 into nums1 in-place.

        Uses a three-pointer approach, filling from the back to avoid
        overwriting elements in nums1 that haven't been processed yet.

        Args:
            nums1: First sorted array with m elements followed by n zeros.
            m: Number of actual elements in nums1.
            nums2: Second sorted array with n elements.
            n: Number of elements in nums2.

        Time Complexity: O(m + n)
        Space Complexity: O(1)
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


class TestMergeSortedArray(unittest.TestCase):
    """Test cases for Merge Sorted Array solution."""

    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()

    def test_basic_merge(self):
        """Test basic merge of two arrays."""
        nums1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(nums1, 3, [2, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_empty_nums2(self):
        """Test when nums2 is empty."""
        nums1 = [1]
        self.solution.merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

    def test_empty_nums1(self):
        """Test when nums1 has no initial elements."""
        nums1 = [0]
        self.solution.merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

    def test_nums2_all_smaller(self):
        """Test when all nums2 elements are smaller."""
        nums1 = [4, 5, 6, 0, 0, 0]
        self.solution.merge(nums1, 3, [1, 2, 3], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_nums2_all_larger(self):
        """Test when all nums2 elements are larger."""
        nums1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(nums1, 3, [4, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_interleaved(self):
        """Test interleaved elements."""
        nums1 = [1, 3, 5, 0, 0, 0]
        self.solution.merge(nums1, 3, [2, 4, 6], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        """Test with duplicate values."""
        nums1 = [1, 2, 2, 0, 0]
        self.solution.merge(nums1, 3, [2, 3], 2)
        self.assertEqual(nums1, [1, 2, 2, 2, 3])


if __name__ == '__main__':
    unittest.main()
