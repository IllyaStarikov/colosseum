#!/usr/bin/env python3
"""
1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice. You can return the answer in any order.

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists

Examples:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]

Edge Cases:
    - Two elements: [1,4], target=5 -> [0,1]
    - Same value twice: [3,3], target=6 -> [0,1]
    - Negative numbers: [-1,-2,-3,-4,-5], target=-8 -> [2,4]
    - Mix positive/negative: [-3,4,3,90], target=0 -> [0,2]
    - Zero in array: [0,4,3,0], target=0 -> [0,3]
    - Answer at end: [1,2,3,4,5], target=9 -> [3,4]
"""

# Pattern: Hash Map (Complement Search)
#     When to use:
#     - Find two elements with a specific relationship (sum, difference)
#     - Need O(1) lookup for previously seen elements
#     - Trading space for time (O(n) space to avoid O(n²) time)
#
#     Telltale signs in this problem:
#     - "two numbers such that they add up to target"
#     - "return indices" (need to track positions, not just values)
#     - Unsorted array (can't use two-pointer without sorting)
#
# Approach:
#     1. BRUTE FORCE: Check every pair (i, j) where i < j
#        - Two nested loops: for each element, scan rest of array
#        - Time: O(n²), Space: O(1)
#
#     2. SORT + TWO POINTERS: Sort array, use left/right pointers
#        - Time: O(n log n), Space: O(n) for index tracking
#        - Loses original indices, need extra bookkeeping
#
#     3. OPTIMAL: Hash map storing {value: index} as we iterate
#        - For each num, check if (target - num) already in map
#        - If found, return both indices; else store current num
#        - Time: O(n), Space: O(n)
#
# Clarifying Questions:
#     - Can there be multiple solutions? (No, exactly one)
#     - Can I use the same element twice? (No)
#     - Return order of indices? (Any order)
#     - Negative numbers? (Yes, -10^9 to 10^9)
#
# Common Mistakes:
#     - Storing complement as key instead of the number itself
#       (need to look up complement, store the number)
#     - Using same element twice (check index != current)
#       (handled naturally by checking before storing)
#     - Forgetting to handle duplicates like [3,3] with target 6
#       (works because we check before adding to map)
#
# Related Problems:
#     - 15. 3Sum (Medium) — fix one element, Two Sum on rest
#     - 18. 4Sum (Medium) — generalization to k elements
#     - 167. Two Sum II (Medium) — sorted array, two-pointer approach
#     - 653. Two Sum IV - BST (Easy) — same pattern on a tree
#
# Follow-up Questions:
#     1. What if array was sorted? (Two-pointer O(1) space, LC 167)
#     2. What if three numbers summing to target? (3Sum: fix one + Two Sum)
#     3. What if multiple valid pairs exist? (Return all, dedupe with set)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices whose values sum to target using hash map.

        Args:
            nums: Array of integers.
            target: Target sum to find.

        Returns:
            List of two indices [i, j] where nums[i] + nums[j] == target.

        Complexity:
            Time: O(n) - single pass, O(1) hash lookups
            Space: O(n) - hash map stores up to n-1 elements
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [i, seen[complement]]
            else:
                seen[num] = i

        return []

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, num in enumerate(nums):
    #         complement = target - num
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == complement:
    #                 return [i, j]
    #     return []


if __name__ == "__main__":
    s = Solution()

    # Example 1: basic case
    result = s.twoSum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1], f"Expected [0,1], got {result}"

    # Example 2: answer not at start
    result = s.twoSum([3, 2, 4], 6)
    assert sorted(result) == [1, 2], f"Expected [1,2], got {result}"

    # Example 3: same element twice
    result = s.twoSum([3, 3], 6)
    assert sorted(result) == [0, 1], f"Expected [0,1], got {result}"

    # Edge: two elements
    result = s.twoSum([1, 4], 5)
    assert sorted(result) == [0, 1], f"Expected [0,1], got {result}"

    # Edge: negative numbers
    result = s.twoSum([-1, -2, -3, -4, -5], -8)
    assert sorted(result) == [2, 4], f"Expected [2,4], got {result}"

    # Edge: mix of positive and negative
    result = s.twoSum([-3, 4, 3, 90], 0)
    assert sorted(result) == [0, 2], f"Expected [0,2], got {result}"

    # Edge: zero in array
    result = s.twoSum([0, 4, 3, 0], 0)
    assert sorted(result) == [0, 3], f"Expected [0,3], got {result}"

    # Edge: target is negative
    result = s.twoSum([5, -7, 2, 1], -5)
    assert sorted(result) == [1, 2], f"Expected [1,2], got {result}"

    # Edge: answer at the end
    result = s.twoSum([1, 2, 3, 4, 5], 9)
    assert sorted(result) == [3, 4], f"Expected [3,4], got {result}"

    # Edge: larger array, answer in middle
    result = s.twoSum([10, 20, 30, 40, 50, 60], 70)
    assert sorted(result) == [0, 5] or sorted(result) == [1, 4] or sorted(result) == [2, 3], f"Got {result}"

    print("All tests passed!")
