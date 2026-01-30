#!/usr/bin/env python3
"""
149. Max Points on a Line (Hard)
https://leetcode.com/problems/max-points-on-a-line/

Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane, return the maximum number of points that lie on the same straight line.

Constraints:
    - 1 <= points.length <= 300
    - points[i].length == 2
    - -10^4 <= xi, yi <= 10^4
    - All points are unique

Examples:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3
    Explanation: All three points are collinear.

    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Edge Cases:
    - Single point: [[1,1]] -> 1
    - Two points: [[1,1],[2,2]] -> 2
    - Empty list: [] -> 0
    - Vertical line: [[1,1],[1,2],[1,3]] -> 3
    - Horizontal line: [[1,1],[2,1],[3,1]] -> 3
    - Duplicate points: [[1,1],[1,1],[2,2]] -> 3
    - All points collinear: [[1,1],[2,2],[3,3],[4,4]] -> 4
    - No three collinear: [[0,0],[1,1],[0,1]] -> 2
"""

# Pattern: Hash Map with Slope Normalization
#     When to use:
#     - Geometry problems involving lines
#     - Counting collinear points
#     - Need to group by slope/direction
#
#     Telltale signs in this problem:
#     - "points on the same straight line"
#     - "maximum number of points"
#     - Working with coordinates
#
# Approach:
#     1. BRUTE FORCE: Check every triplet of points for collinearity
#        - Time: O(n^3), Space: O(1)
#
#     2. OPTIMAL: For each anchor point, count slopes to all other points
#        - Insight: Points on same line through anchor have same slope
#        - Use GCD to normalize slope as fraction (avoid floating-point issues)
#        - Handle vertical lines (dx=0) and duplicates separately
#        - Time: O(n^2), Space: O(n)
#
# Clarifying Questions:
#     - Are all points unique? (Constraints say yes, but some variants allow duplicates)
#     - Can points be negative? (Yes, -10^4 to 10^4)
#     - What about floating-point precision? (Use GCD normalization instead)
#     - Single point result? (Return 1)
#     - Empty input? (Return 0)
#
# Common Mistakes:
#     - Using floating-point for slope (precision issues)
#     - Not handling vertical lines (slope undefined)
#     - Not handling duplicate points
#     - Not normalizing slope sign (e.g., -1/2 vs 1/-2)
#     - Forgetting to count the anchor point itself
#
# Related Problems:
#     - 356. Line Reflection (Medium) - geometry with slopes
#     - 447. Number of Boomerangs (Medium) - distance-based geometry
#     - 939. Minimum Area Rectangle (Medium) - coordinate geometry
#
# Follow-up Questions:
# 1. How would you handle floating-point precision without GCD?
# 2. What if we needed to return the actual points on the line?
# 3. How would you parallelize this algorithm?

from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Find maximum number of points on the same line.

        Uses anchor point approach: for each point, count slopes to all other
        points using GCD-reduced fractions to avoid floating-point issues.

        Args:
            points: List of [x, y] coordinate pairs.

        Returns:
            Maximum number of points that lie on the same line.

        Complexity:
            Time: O(n^2) - for each point, compute slopes to all others
            Space: O(n) - slope counter at each anchor
        """
        n = len(points)
        if n <= 2:
            return n

        result = 0

        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # Normalize slope using GCD to avoid floating-point issues
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # Ensure consistent sign (dx positive, or dx=0 and dy positive)
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                slopes[(dx, dy)] += 1

            local_max = duplicates
            for count in slopes.values():
                local_max = max(local_max, count + duplicates)

            result = max(result, local_max)

        return result


# # Previous O(n^3) solution using line equations - TLE on large inputs
# from collections import namedtuple, Counter
# from decimal import Decimal
#
# Line = namedtuple('Line', "m b")
#
# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         if len(points) < 2:
#             return len(points)
#
#         lines = self._generate_all_lines(points)
#         lines_counter = Counter()
#
#         for line in lines:
#             for point in points:
#                 x, y = point
#                 m, b = line
#
#                 if b is None:
#                     if x == m:
#                         lines_counter[line] += 1
#                 elif abs(y - b - m * x) < 0.1 ** 15:
#                     lines_counter[line] += 1
#
#         return lines_counter.most_common(1)[0][1]
#
#     def _generate_all_lines(self, points: List[List[int]]) -> List[Line]:
#         lines = set()
#         length = len(points)
#
#         for i, point_1 in enumerate(points):
#             for j, point_2 in enumerate(points):
#                 if i == j:
#                     break
#
#                 x_1, y_1 = point_1
#                 x_2, y_2 = point_2
#
#                 is_vertical = x_2 - x_1 == 0
#
#                 m = Decimal(x_2) if is_vertical else Decimal(y_2 - y_1) / Decimal(x_2 - x_1)
#                 b = None if is_vertical else Decimal(y_2 - m * x_2)
#                 lines.add(Line(m, b))
#
#         return lines


if __name__ == "__main__":
    s = Solution()

    # Example 1: Three collinear points
    assert s.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3, "Collinear points failed"

    # Example 2: Not all on same line
    assert s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4, "Mixed points failed"

    # Edge case: Single point
    assert s.maxPoints([[1, 1]]) == 1, "Single point failed"

    # Edge case: Two points
    assert s.maxPoints([[1, 1], [2, 2]]) == 2, "Two points failed"

    # Edge case: Vertical line
    assert s.maxPoints([[1, 1], [1, 2], [1, 3]]) == 3, "Vertical line failed"

    # Edge case: Horizontal line
    assert s.maxPoints([[1, 1], [2, 1], [3, 1]]) == 3, "Horizontal line failed"

    # Edge case: Empty list
    assert s.maxPoints([]) == 0, "Empty list failed"

    # Edge case: Duplicate points
    assert s.maxPoints([[1, 1], [1, 1], [2, 2]]) == 3, "Duplicate points failed"

    # Edge case: No three collinear
    assert s.maxPoints([[0, 0], [1, 1], [0, 1]]) == 2, "No three collinear failed"

    # Negative coordinates
    assert s.maxPoints([[-1, -1], [0, 0], [1, 1]]) == 3, "Negative coordinates failed"

    print("All tests passed!")
