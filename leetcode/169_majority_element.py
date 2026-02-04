#!/usr/bin/env python3
"""
169. Majority Element (Easy)
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n / 2 times.
You may assume that the majority element always exists in the array.

Constraints:
    - n == nums.length
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

Examples:
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Edge Cases:
    - Single element: [1] -> 1
    - All identical: [5,5,5,5] -> 5
    - Two same elements: [3,3] -> 3
    - Two elements, one majority: [1,2,1] -> 1
    - Minimum majority (n//2 + 1 occurrences): [1,2,3,1,1] -> 1
    - Negative numbers: [-1,-1,2] -> -1
"""

# Pattern: Boyer-Moore Voting
#     When to use:
#     - Finding element with frequency > n/k
#     - O(1) space constraint on a frequency problem
#     - Stream/online processing where you can't store all elements
#
#     Telltale signs in this problem:
#     - "appears more than n/2 times"
#     - "majority element always exists"
#     - Follow-up asks for O(1) space
#
# Approach:
#     1. BRUTE FORCE: Count each element's frequency with a hash map
#        - Time: O(n), Space: O(n)
#
#     2. SORTING: Sort and return middle element (index n//2)
#        - Insight: majority occupies > half the array, so it must be at the middle
#        - Time: O(n log n), Space: O(n)
#
#     3. OPTIMAL: Boyer-Moore Voting Algorithm
#        - Insight: majority element survives cancellation against all others combined
#        - Maintain a candidate and count; when count hits 0, pick new candidate
#        - Matching elements increment, mismatches decrement
#        - Time: O(n), Space: O(1)
#
# Clarifying Questions:
#     - Is a majority element guaranteed to exist? (Yes, per problem statement)
#     - Can the array be empty? (No, n >= 1 per constraints)
#     - Can values be negative? (Yes, -10^9 to 10^9)
#     - If majority not guaranteed, do we need a verification pass? (Not here, but yes in general)
#
# Common Mistakes:
#     - Forgetting to set count = 1 when picking a new candidate
#     - Not resetting count when switching candidates in sort+scan approach
#     - Using extra space when O(1) is required
#     - Assuming Boyer-Moore works without a majority guarantee (need verification pass)
#
# Related Problems:
#     - 229. Majority Element II (Medium) - elements appearing > n/3 times, 2 candidates
#     - 347. Top K Frequent Elements (Medium) - general frequency problem
#     - 1150. Check If a Number Is Majority Element in a Sorted Array (Easy)
#
# Follow-up Questions:
#     1. What if majority not guaranteed? (Add a second pass to verify candidate count)
#     2. Find all elements appearing > n/3 times? (LC 229, track 2 candidates)
#     3. Generalize to > n/k? (Track k-1 candidates, k-1 counters)

# import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find majority element using Boyer-Moore Voting Algorithm.

        Args:
            nums: Integer array with a guaranteed majority element.

        Returns:
            The element appearing more than n/2 times.

        Complexity:
            Time: O(n) - single pass, every element visited exactly once
            Space: O(1) - two variables regardless of input size
        """
        count: int = 0
        candidate: int = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate

    # def majorityElement(self, nums: List[int]) -> int:
    #     return sorted(nums)[len(nums) // 2]

    # def majorityElement(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     max_value, max_element = 0, 0
    #     current_value, current_element = 0, nums[0]
    #
    #     for element in nums:
    #         if element != current_element:
    #             current_element = element
    #             current_value = 1
    #         else:
    #             current_value += 1
    #
    #         if current_value > max_value:
    #             max_value = current_value
    #             max_element = current_element
    #
    #     return max_element


    # def majorityElement(self, nums: List[int]) -> int:
    #     return collections.Counter(nums).most_common(1)[0][0]


if __name__ == "__main__":
    s = Solution()

    # Example 1: basic majority
    assert s.majorityElement([3, 2, 3]) == 3

    # Example 2: clear majority
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

    # Single element
    assert s.majorityElement([1]) == 1

    # All same elements
    assert s.majorityElement([5, 5, 5, 5]) == 5

    # Two same elements
    assert s.majorityElement([3, 3]) == 3

    # Two elements, one majority
    assert s.majorityElement([1, 2, 1]) == 1

    # Majority at minimum threshold (appears exactly n//2 + 1 times)
    assert s.majorityElement([1, 2, 3, 1, 1]) == 1

    # Majority in first group (previously failed: [1,1,1,2,2] returned 2)
    assert s.majorityElement([1, 1, 1, 2, 2]) == 1

    # Negative numbers
    assert s.majorityElement([-1, -1, 2]) == -1

    print("All tests passed!")
