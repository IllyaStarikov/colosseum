#!/usr/bin/env python3
"""
80. Remove Duplicates from Sorted Array II (Medium)
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k
elements of nums should hold the final result. It does not matter what you
leave beyond the first k elements. Return k.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums is sorted in non-decreasing order

Examples:
    Input: [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]

    Input: [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]

Edge Cases:
    - Single element: [1] -> 1
    - Two elements (same): [1,1] -> 2
    - Two elements (different): [1,2] -> 2
    - All identical: [5,5,5,5,5] -> 2
    - No duplicates: [1,2,3,4,5] -> 5
    - Negatives: [-3,-3,-3,-1] -> 3
"""

# Pattern: Two-Pointer (Fast/Slow aka Read/Write)
#     When to use:
#     - Sorted array problems requiring in-place modification
#     - Removing or rearranging elements with O(1) space
#
#     Telltale signs in this problem:
#     - "sorted in non-decreasing order"
#     - "remove duplicates in-place"
#     - "O(1) extra memory"
#     - "at most twice" (generalizes to "at most k")
#
# Approach:
#     1. BRUTE FORCE: Count occurrences with a hash map, rebuild array
#        - Time: O(n), Space: O(n) — violates space constraint
#
#     2. OPTIMAL: Two pointers — write_i marks where to place next valid
#        element, read_i scans forward
#        - Insight: since array is sorted, duplicates are adjacent.
#          Compare nums[read_i] to nums[write_i - 2]. If equal, writing
#          it would create a triple — skip it.
#        - First 2 elements are always valid (at most 2 allowed).
#        - Time: O(n), Space: O(1)
#
# Clarifying Questions:
#     - Can I modify the input array? (Yes, in-place required)
#     - What about elements after index k? (Don't matter)
#     - Empty array possible? (No, n >= 1 per constraints)
#     - Does "at most twice" mean exactly twice or up to twice? (Up to)
#
# Common Mistakes:
#     - Using `and` instead of just checking nums[write_i - 2]
#       (checking both write_i-1 AND write_i-2 rejects valid pairs)
#     - Starting loop at index 0 or 1 instead of 2
#     - Forgetting the early return for len <= 2
#     - Comparing against the read pointer's neighbors instead of the
#       write pointer's (must compare against what's already written)
#
# Related Problems:
#     - 26. Remove Duplicates from Sorted Array (Easy) — at most 1 of each
#     - 27. Remove Element (Easy) — remove all of a target value
#     - 283. Move Zeroes (Easy) — similar in-place read/write pattern
#
# Follow-up Questions:
#     1. What if "at most twice" was "at most k"? (Change write_i=k,
#        range(k,...), compare nums[write_i - k])
#     2. What if the array wasn't sorted? (Can't use this trick —
#        would need a hash map, O(n) space)
#     3. Is the early return guard necessary? (No — loop body is safe,
#        but it avoids unnecessary work and makes intent clear)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove excess duplicates using read/write two-pointer technique.

        Args:
            nums: Sorted integer array (modified in-place).

        Returns:
            Count k of valid elements. First k elements of nums contain
            the result where each unique value appears at most twice.

        Complexity:
            Time: O(n) - single pass, every element visited exactly once
            Space: O(1) - two integer pointers only
        """
        if len(nums) <= 2:
            return len(nums)

        write_i = 2
        for read_i in range(2, len(nums)):
            if nums[read_i] != nums[write_i - 2]:
                nums[write_i] = nums[read_i]
                write_i += 1

        return write_i


if __name__ == "__main__":
    s = Solution()

    # Example 1: basic duplicates
    nums = [1, 1, 1, 2, 2, 3]
    k = s.removeDuplicates(nums)
    assert k == 5, f"Expected 5, got {k}"
    assert nums[:k] == [1, 1, 2, 2, 3], f"Expected [1,1,2,2,3], got {nums[:k]}"

    # Example 2: more duplicates
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = s.removeDuplicates(nums)
    assert k == 7, f"Expected 7, got {k}"
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3], f"Expected [0,0,1,1,2,3,3], got {nums[:k]}"

    # Edge: exactly two elements (same)
    nums = [1, 1]
    k = s.removeDuplicates(nums)
    assert k == 2, f"Expected 2, got {k}"
    assert nums[:k] == [1, 1], f"Expected [1,1], got {nums[:k]}"

    # Edge: exactly two elements (different)
    nums = [1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2, f"Expected 2, got {k}"
    assert nums[:k] == [1, 2], f"Expected [1,2], got {nums[:k]}"

    # Edge: single element
    nums = [1]
    k = s.removeDuplicates(nums)
    assert k == 1, f"Expected 1, got {k}"
    assert nums[:k] == [1], f"Expected [1], got {nums[:k]}"

    # Edge: all same
    nums = [5, 5, 5, 5, 5]
    k = s.removeDuplicates(nums)
    assert k == 2, f"Expected 2, got {k}"
    assert nums[:k] == [5, 5], f"Expected [5,5], got {nums[:k]}"

    # Edge: no duplicates at all
    nums = [1, 2, 3, 4, 5]
    k = s.removeDuplicates(nums)
    assert k == 5, f"Expected 5, got {k}"
    assert nums[:k] == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {nums[:k]}"

    # Edge: negatives
    nums = [-3, -3, -3, -1, 0, 0, 0, 2]
    k = s.removeDuplicates(nums)
    assert k == 6, f"Expected 6, got {k}"
    assert nums[:k] == [-3, -3, -1, 0, 0, 2], f"Expected [-3,-3,-1,0,0,2], got {nums[:k]}"

    # Edge: long run of one value then another
    nums = [1, 1, 1, 1, 2, 2, 2, 2]
    k = s.removeDuplicates(nums)
    assert k == 4, f"Expected 4, got {k}"
    assert nums[:k] == [1, 1, 2, 2], f"Expected [1,1,2,2], got {nums[:k]}"

    print("All tests passed!")
