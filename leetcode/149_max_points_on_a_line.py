#!/usr/bin/env python3
"""149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Find the maximum number of points that lie on the same straight line.

Author: Illya Starikov
Date: 08/12/19
License: MIT
"""

from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    """Solution for the Max Points on a Line problem."""

    def maxPoints(self, points: List[List[int]]) -> int:
        """Find maximum number of points on the same line.

        Uses anchor point approach: for each point, count slopes to all other
        points using GCD-reduced fractions to avoid floating-point issues.

        Args:
            points: List of [x, y] coordinate pairs.

        Returns:
            Maximum number of points that lie on the same line.

        Time Complexity: O(n^2) where n is the number of points
            - For each point, compute slopes to all other points
        Space Complexity: O(n) for the slope counter at each anchor
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


import unittest


class TestMaxPointsOnALine(unittest.TestCase):
    """Test cases for Max Points on a Line solution."""

    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()

    def test_three_points_on_line(self):
        """Test three collinear points."""
        points = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_not_all_on_same_line(self):
        """Test points not all on the same line."""
        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        self.assertEqual(self.solution.maxPoints(points), 4)

    def test_single_point(self):
        """Test single point."""
        points = [[1, 1]]
        self.assertEqual(self.solution.maxPoints(points), 1)

    def test_two_points(self):
        """Test two points."""
        points = [[1, 1], [2, 2]]
        self.assertEqual(self.solution.maxPoints(points), 2)

    def test_vertical_line(self):
        """Test points on a vertical line."""
        points = [[1, 1], [1, 2], [1, 3]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_horizontal_line(self):
        """Test points on a horizontal line."""
        points = [[1, 1], [2, 1], [3, 1]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_empty_list(self):
        """Test empty list of points."""
        points = []
        self.assertEqual(self.solution.maxPoints(points), 0)

    def test_duplicate_points(self):
        """Test duplicate points."""
        points = [[1, 1], [1, 1], [2, 2]]
        self.assertEqual(self.solution.maxPoints(points), 3)


if __name__ == '__main__':
    unittest.main()