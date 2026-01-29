#!/usr/bin/env python3
"""
27. Remove Element
https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Return the number
of elements in nums which are not equal to val.

Author: Illya Starikov
Date: 2026-01-28
License: MIT
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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


if __name__ == "__main__":
    s = Solution()

    # Example 1: nums = [3,2,2,3], val = 3 → k = 2, nums = [2,2]
    nums = [3, 2, 2, 3]
    k = s.removeElement(nums, 3)
    assert k == 2, f"Expected 2, got {k}"
    assert sorted(nums[:k]) == [2, 2], f"Expected [2, 2], got {nums[:k]}"

    # Example 2: nums = [0,1,2,2,3,0,4,2], val = 2 → k = 5, nums = [0,1,3,0,4]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums, 2)
    assert k == 5, f"Expected 5, got {k}"
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4], f"Expected [0, 0, 1, 3, 4], got {nums[:k]}"

    # Edge case: empty array
    nums = []
    k = s.removeElement(nums, 1)
    assert k == 0, f"Expected 0, got {k}"

    # Edge case: no elements to remove
    nums = [1, 2, 3]
    k = s.removeElement(nums, 4)
    assert k == 3, f"Expected 3, got {k}"
    assert sorted(nums[:k]) == [1, 2, 3], f"Expected [1, 2, 3], got {nums[:k]}"

    # Edge case: all elements should be removed
    nums = [3, 3, 3]
    k = s.removeElement(nums, 3)
    assert k == 0, f"Expected 0, got {k}"

    # Edge case: single element (matches)
    nums = [3]
    k = s.removeElement(nums, 3)
    assert k == 0, f"Expected 0, got {k}"

    # Edge case: single element (doesn't match)
    nums = [3]
    k = s.removeElement(nums, 1)
    assert k == 1, f"Expected 1, got {k}"
    assert nums[0] == 3, f"Expected [3], got {nums[:k]}"

    print("All tests passed!")
