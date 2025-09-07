#!/usr/bin/env python3
"""Tests for LeetCode Problem 149: Max Points on a Line.

Author: Illya Starikov
Date: 08/12/19
License: MIT
"""

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
solution_module = __import__("149_max_points_on_a_line")


class TestMaxPointsOnALine(unittest.TestCase):
    """Test cases for Max Points on a Line solution."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = solution_module.Solution()
    
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