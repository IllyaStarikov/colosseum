#!/usr/local/bin/python3
#
# bijele.py
# Desktop
#
# Created by Illya Starikov on 06/10/17.
# Copyright 2017. Illya Starikov. All rights reserved.
#

proper_values = [1, 1, 2, 2, 2, 8]
values = [int(x) for x in input().split(" ")]

solution = []
for index, value in enumerate(values):
    solution += [str(proper_values[index] - value)]

print(' '.join(solution))
