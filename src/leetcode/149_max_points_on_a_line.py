#!/usr/bin/env python3
"""LeetCode Problem 149: Max Points on a Line.

Find the maximum number of points that lie on the same straight line.

Author: Illya Starikov
Date: 08/12/19
License: MIT
"""

from collections import namedtuple, Counter
from decimal import Decimal
from typing import List

Line = namedtuple('Line', "m b")


class Solution:
    """Solution for the Max Points on a Line problem."""
    
    def maxPoints(self, points: List[List[int]]) -> int:
        """Find maximum number of points on the same line.
        
        Args:
            points: List of [x, y] coordinate pairs.
            
        Returns:
            Maximum number of points that lie on the same line.
            
        Time Complexity: O(n^3) where n is the number of points
            - O(n^2) to generate all lines between point pairs
            - O(n) to check each point against each line
        Space Complexity: O(n^2) for storing all possible lines
        """
        if len(points) < 2:
            return len(points)
        
        lines = self._generate_all_lines(points)
        lines_counter = Counter()
        
        for line in lines:
            for point in points:
                x, y = point
                m, b = line
                
                if b is None:
                    if x == m:
                        lines_counter[line] += 1
                elif abs(y - b - m * x) < 0.1 ** 15:
                    lines_counter[line] += 1
        
        return lines_counter.most_common(1)[0][1]
    
    def _generate_all_lines(self, points: List[List[int]]) -> List[Line]:
        """Generate all unique lines from point pairs.
        
        Args:
            points: List of [x, y] coordinate pairs.
            
        Returns:
            List of unique lines defined by slope and y-intercept.
            
        Time Complexity: O(n^2) where n is the number of points
        Space Complexity: O(n^2) for storing unique lines
        """
        lines = set()
        length = len(points)
        
        for i, point_1 in enumerate(points):
            for j, point_2 in enumerate(points):
                if i == j:
                    break
                
                x_1, y_1 = point_1
                x_2, y_2 = point_2
                
                is_vertical = x_2 - x_1 == 0
                
                m = Decimal(x_2) if is_vertical else Decimal(y_2 - y_1) / Decimal(x_2 - x_1)
                b = None if is_vertical else Decimal(y_2 - m * x_2)
                lines.add(Line(m, b))

        return lines


# CLAUDE-CODE BEGIN
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
# CLAUDE-CODE END