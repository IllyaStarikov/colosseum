#!/usr/local/bin/python3
#
# guess-the-data-structure.py
# Illya
#
# Created by Illya Starikov on 06/04/17.
# Copyright 2017. Illya Starikov. All rights reserved.
#

from collections import deque
import sys


def get_value(x):
    return {
        0: "stack",
        1: "queue",
        2: "priority queue",
    }[x]


PUT_IN_BAG, TAKE_OUT_BAG = 1, 2

line = sys.stdin.readline()
while line:
    test_cases = int(line)

    stack, queue, priority_queue = [], deque([]), []
    data_structures_possibility = [True, True, True]

    for _ in range(test_cases):
        action, value = map(int, sys.stdin.readline().split())

        if action == PUT_IN_BAG:
            stack.append(value)
            queue.append(value)
            priority_queue.append(value)
        elif action == TAKE_OUT_BAG:
            try:
                if data_structures_possibility[0] is True:
                    if not stack or stack.pop() != value:
                        data_structures_possibility[0] = False

                if data_structures_possibility[1] is True:
                    if not queue or queue.popleft() != value:
                        data_structures_possibility[1] = False

                if data_structures_possibility[2] is True:
                    if not priority_queue or max(priority_queue) != value:
                        data_structures_possibility[2] = False
                    else:
                        priority_queue.remove(max(priority_queue))
            except:
                pass
    filtered_for_true = list(filter(lambda x: x is True, data_structures_possibility))

    if len(filtered_for_true) == 0:
        print("impossible")
    elif len(filtered_for_true) == 1:
        index = data_structures_possibility.index(True)
        print(get_value(index))
    else:
        print("not sure")

    line=sys.stdin.readline()
