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

    # Edge case: two elements same, both removed
    nums = [3, 3]
    k = s.removeElement(nums, 3)
    assert k == 0, f"Expected 0, got {k}"

    # Edge case: two elements different, one removed
    nums = [1, 2]
    k = s.removeElement(nums, 1)
    assert k == 1, f"Expected 1, got {k}"
    assert nums[0] == 2, f"Expected [2], got {nums[:k]}"

    print("All tests passed!")
