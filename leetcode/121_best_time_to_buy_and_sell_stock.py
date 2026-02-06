#!/usr/bin/env python3
"""
121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock
on the ith day. You want to maximize your profit by choosing a single day to
buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4

Examples:
    Input: [7,1,5,3,6,4]
    Output: 5 (buy day 2 at 1, sell day 5 at 6)

    Input: [7,6,4,3,1]
    Output: 0 (prices only decrease, no profit possible)

Edge Cases:
    - Single element: [5] -> 0
    - Two elements (profit): [1,2] -> 1
    - Two elements (no profit): [2,1] -> 0
    - Two elements (same): [3,3] -> 0
    - All identical: [5,5,5,5] -> 0
    - All decreasing: [7,6,4,3,1] -> 0
    - Best buy first day: [1,4,2,7] -> 6
    - Best buy last possible: [5,3,1,8] -> 7
"""

# Pattern: Greedy / One-Pass Min Tracking
#     When to use:
#     - Find max difference where smaller element comes before larger
#     - Single-pass optimization over a sequence
#     - "Best" or "maximum" profit/gain problems
#
#     Telltale signs in this problem:
#     - "maximize your profit"
#     - "choose a single day to buy... a different day in the future to sell"
#     - Single transaction constraint (simplifies to tracking running min)
#
# Approach:
#     1. BRUTE FORCE: Check every (buy, sell) pair where buy < sell
#        - Two nested loops: for each buy day, check all future sell days
#        - Time: O(n^2), Space: O(1)
#
#     2. RECURSIVE: For each day, either buy here (max future - price) or skip
#        - max(max(prices[1:]) - prices[0], recurse(prices[1:]))
#        - Time: O(n^2) due to max() + slicing at each level, Space: O(n^2)
#
#     3. OPTIMAL: Single pass tracking minimum price seen so far
#        - Insight: at each price, the best profit if selling today is
#          price - min_so_far. Track the global max of this.
#        - Time: O(n), Space: O(1)
#
# Clarifying Questions:
#     - Can I buy and sell on the same day? (Yes but profit = 0, pointless)
#     - Must I make a transaction? (No, return 0 if no profit possible)
#     - Can prices be 0? (Yes, 0 <= prices[i] <= 10^4)
#     - Multiple transactions? (No, exactly one buy and one sell)
#
# Common Mistakes:
#     - Initializing min_price to 0 instead of prices[0] or infinity
#       (0 is below all valid prices, so min never updates)
#     - Tracking max price instead of min price (need min before max)
#     - Forgetting that buy must come before sell (can't just do
#       max(prices) - min(prices) if max comes before min)
#     - Using O(n) space with prefix arrays when not needed
#
# Related Problems:
#     - 122. Best Time to Buy and Sell Stock II (Medium) — unlimited transactions
#     - 123. Best Time to Buy and Sell Stock III (Hard) — at most 2 transactions
#     - 53. Maximum Subarray (Medium) — similar running-min/max pattern
#       (Kadane's algorithm is the same idea applied to subarray sums)
#
# Follow-up Questions:
#     1. What if unlimited transactions? (LC 122 — greedy: sum all
#        positive day-over-day differences)
#     2. What if at most k transactions? (LC 188 — DP with transaction
#        state tracking)
#     3. How does this relate to Kadane's / Maximum Subarray? (Convert
#        prices to daily deltas; max profit = max subarray sum of deltas)

from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find max profit from a single buy/sell using one-pass min tracking.

        Args:
            prices: List of stock prices by day.

        Returns:
            Maximum profit from one transaction, or 0 if none profitable.

        Complexity:
            Time: O(n) - single pass through prices
            Space: O(1) - two variables only
        """
        min_current = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_current:
                min_current = price

            profit = price - min_current
            if profit > max_profit:
                max_profit = profit

        return max_profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) == 1:
    #         return 0
    #
    #     return max(
    #         max(prices[1:]) - prices[0],
    #         self.maxProfit(prices[1:])
    #     )


class TestSolution(unittest.TestCase):
    """Tests for Best Time to Buy and Sell Stock solution."""

    def setUp(self):
        """Create Solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Example 1: buy day 2 (price 1), sell day 5 (price 6)."""
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_example_2(self):
        """Example 2: prices only decrease, no profit possible."""
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_edge_single_element(self):
        """Single element, can't trade."""
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_edge_two_elements_profit(self):
        """Two elements, profit possible."""
        self.assertEqual(self.solution.maxProfit([1, 2]), 1)

    def test_edge_two_elements_no_profit(self):
        """Two elements, no profit."""
        self.assertEqual(self.solution.maxProfit([2, 1]), 0)

    def test_edge_two_elements_same(self):
        """Two elements, same price."""
        self.assertEqual(self.solution.maxProfit([3, 3]), 0)

    def test_edge_all_same(self):
        """All same prices."""
        self.assertEqual(self.solution.maxProfit([5, 5, 5, 5]), 0)

    def test_edge_best_buy_first(self):
        """Best buy is first day."""
        self.assertEqual(self.solution.maxProfit([1, 4, 2, 7]), 6)

    def test_edge_best_buy_late(self):
        """Best buy is late in array."""
        self.assertEqual(self.solution.maxProfit([5, 3, 1, 8]), 7)

    def test_edge_profit_at_end(self):
        """Profit realized at the very end."""
        self.assertEqual(self.solution.maxProfit([3, 2, 1, 4]), 3)

    def test_edge_multiple_peaks(self):
        """Multiple peaks, pick best single transaction."""
        self.assertEqual(self.solution.maxProfit([3, 1, 4, 1, 5, 9, 2, 6]), 8)

    def test_edge_large_values(self):
        """Large values at constraint boundary."""
        self.assertEqual(self.solution.maxProfit([10000, 1, 10000]), 9999)


if __name__ == "__main__":
    unittest.main()
