#!/usr/bin/env python3
"""
189. Rotate Array (Medium)
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Constraints:
    - 1 <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1
    - 0 <= k <= 10^5

Examples:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 step: [7,1,2,3,4,5,6]
        rotate 2 steps: [6,7,1,2,3,4,5]
        rotate 3 steps: [5,6,7,1,2,3,4]

    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]

Edge Cases:
    - k = 0: no rotation, array unchanged
    - k = len(nums): full rotation, array unchanged
    - k > len(nums): same as k % len(nums)
    - Single element: [1], k=1 -> [1]
    - Two elements: [1,2], k=1 -> [2,1]
    - All identical: [5,5,5], k=2 -> [5,5,5]
"""

# Pattern: Array Reversal / Cyclic Replacement
#     When to use:
#     - In-place array rotation
#     - O(1) space constraint
#     - Cyclic shifting of elements
#
#     Telltale signs in this problem:
#     - "rotate the array to the right by k steps"
#     - "modify nums in-place"
#     - Follow-up asks for O(1) space
#
# Approach:
#     1. BRUTE FORCE: Rotate one step at a time, k times
#        - Move last element to front, shift rest right
#        - Time: O(n * k), Space: O(1)
#
#     2. EXTRA ARRAY: Copy to new array at rotated positions
#        - new[(i + k) % n] = nums[i]
#        - Time: O(n), Space: O(n)
#
#     3. OPTIMAL: Three reverses
#        - Insight: Rotating right by k is same as:
#          1. Reverse entire array
#          2. Reverse first k elements
#          3. Reverse remaining n-k elements
#        - Example: [1,2,3,4,5,6,7], k=3
#          -> [7,6,5,4,3,2,1] (reverse all)
#          -> [5,6,7,4,3,2,1] (reverse first 3)
#          -> [5,6,7,1,2,3,4] (reverse last 4)
#        - Time: O(n), Space: O(1)
#
#     4. CYCLIC REPLACEMENT: Move each element to final position
#        - Start at index 0, move to (0+k)%n, continue cycle
#        - Handle multiple cycles when gcd(n,k) > 1
#        - Time: O(n), Space: O(1)
#
# Clarifying Questions:
#     - Modify in-place? (Yes)
#     - Can k be larger than array length? (Yes, use k % n)
#     - Can k be 0? (Yes, no rotation needed)
#     - Negative k? (No, k >= 0 per constraints)
#
# Common Mistakes:
#     - Forgetting to handle k >= n (must use k % n)
#     - Off-by-one errors in reverse boundaries
#     - Not handling k = 0 case (though it works naturally)
#     - Using O(n) space when O(1) is required
#
# Related Problems:
#     - 61. Rotate List (Medium) - linked list rotation
#     - 186. Reverse Words in a String II (Medium) - similar reversal trick
#     - 796. Rotate String (Easy) - string rotation check
#
# Follow-up Questions:
#     1. Can you do it in-place with O(1) extra space? (Yes, three reverses)
#     2. How would you rotate left instead of right? (k = n - k)
#     3. What if you could only swap adjacent elements? (Bubble-like, O(n*k))

from typing import List
import unittest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate array right by k steps using three-reverse technique.

        Args:
            nums: Integer array (modified in-place).
            k: Number of steps to rotate right.

        Complexity:
            Time: O(n) - each element swapped at most twice
            Space: O(1) - only pointer variables
        """
        n = len(nums)
        k = k % n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     k = k % len(nums)  # for k >= len(nums)
    #     write_buffer = []
    #
    #     for i, num in enumerate(nums):
    #         if i < k:
    #             write_buffer.append(num)
    #             nums[i] = nums[len(nums) - k + i]
    #         else:
    #             write_buffer.append(num)
    #             nums[i] = write_buffer.pop(0)


class TestSolution(unittest.TestCase):
    """Tests for Rotate Array solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Example 1: [1,2,3,4,5,6,7], k=3 -> [5,6,7,1,2,3,4]."""
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.solution.rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_example_2(self):
        """Example 2: [-1,-100,3,99], k=2 -> [3,99,-1,-100]."""
        nums = [-1, -100, 3, 99]
        self.solution.rotate(nums, 2)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_edge_k_zero(self):
        """k=0 means no rotation."""
        nums = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_edge_k_equals_length(self):
        """k equals array length, no effective rotation."""
        nums = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, 5)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_edge_k_greater_than_length(self):
        """k > array length, effectively k % n."""
        nums = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, 7)  # Same as k=2
        self.assertEqual(nums, [4, 5, 1, 2, 3])

    def test_edge_single_element(self):
        """Single element unchanged regardless of k."""
        nums = [1]
        self.solution.rotate(nums, 1)
        self.assertEqual(nums, [1])

    def test_edge_single_element_large_k(self):
        """Single element with large k."""
        nums = [42]
        self.solution.rotate(nums, 100)
        self.assertEqual(nums, [42])

    def test_edge_two_elements(self):
        """Two elements, k=1."""
        nums = [1, 2]
        self.solution.rotate(nums, 1)
        self.assertEqual(nums, [2, 1])

    def test_edge_two_elements_k_2(self):
        """Two elements, k=2 (full rotation)."""
        nums = [1, 2]
        self.solution.rotate(nums, 2)
        self.assertEqual(nums, [1, 2])

    def test_edge_all_identical(self):
        """All identical elements."""
        nums = [5, 5, 5, 5]
        self.solution.rotate(nums, 2)
        self.assertEqual(nums, [5, 5, 5, 5])

    def test_edge_negative_numbers(self):
        """Array with negative numbers."""
        nums = [-1, -2, -3, -4]
        self.solution.rotate(nums, 1)
        self.assertEqual(nums, [-4, -1, -2, -3])

    def test_edge_k_one(self):
        """k=1, rotate by single step."""
        nums = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, 1)
        self.assertEqual(nums, [5, 1, 2, 3, 4])

    def test_edge_k_n_minus_one(self):
        """k = n-1, all but one step."""
        nums = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, 4)
        self.assertEqual(nums, [2, 3, 4, 5, 1])

    def test_edge_large_values(self):
        """Values at constraint boundaries."""
        nums = [2**31 - 1, -(2**31), 0]
        self.solution.rotate(nums, 1)
        self.assertEqual(nums, [0, 2**31 - 1, -(2**31)])


if __name__ == "__main__":
    unittest.main()
