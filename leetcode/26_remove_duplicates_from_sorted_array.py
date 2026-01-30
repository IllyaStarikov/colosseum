#!/usr/bin/env python3
"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. Return k (the number of
unique elements), and modify the array so the first k elements contain unique
values in sorted order.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- Array is sorted in non-decreasing order

Author: Illya Starikov
Date: 2026-01-28
License: MIT
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_i = 1
        for read_i in range(1, len(nums)):
            if nums[read_i] != nums[write_i - 1]:
                nums[write_i] = nums[read_i]
                write_i += 1

        return write_i


if __name__ == "__main__":
    s = Solution()

    # Example 1: nums = [1,1,2] -> k = 2, nums[:k] = [1,2]
    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2], f"Example 1 failed: k={k}, nums[:k]={nums[:k]}"

    # Example 2: nums = [0,0,1,1,1,2,2,3,3,4] -> k = 5, nums[:k] = [0,1,2,3,4]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4], f"Example 2 failed: k={k}, nums[:k]={nums[:k]}"

    # Single element
    nums = [1]
    k = s.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1], f"Single element failed: k={k}, nums[:k]={nums[:k]}"

    # No duplicates
    nums = [1, 2, 3, 4, 5]
    k = s.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [1, 2, 3, 4, 5], f"No duplicates failed: k={k}, nums[:k]={nums[:k]}"

    # All same
    nums = [1, 1, 1, 1, 1]
    k = s.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1], f"All same failed: k={k}, nums[:k]={nums[:k]}"

    # Negative numbers
    nums = [-3, -3, -1, 0, 0, 2]
    k = s.removeDuplicates(nums)
    assert k == 4 and nums[:k] == [-3, -1, 0, 2], f"Negative numbers failed: k={k}, nums[:k]={nums[:k]}"

    # Two elements same
    nums = [1, 1]
    k = s.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1], f"Two same failed: k={k}, nums[:k]={nums[:k]}"

    # Two elements different
    nums = [1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2], f"Two different failed: k={k}, nums[:k]={nums[:k]}"

    print("All tests passed!")
