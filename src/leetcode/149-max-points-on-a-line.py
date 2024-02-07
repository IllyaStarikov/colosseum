#!/usr/local/bin/python3
#
# 149-max-points-on-a-line.py
# leetcode
#
# Created by Illya Starikov on 08/12/19.
# Copyright 2019. Illya Starikov. MIT License.
#


from collections import namedtuple, Counter
from decimal import Decimal

Line = namedtuple('Line', "m b")


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
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
