#!/usr/local/bin/python3
#
# 8.1-triple-step.py
# chapter-8
#
# Created by Illya Starikov on 07/24/19.
# Copyright 2019. Illya Starikov. MIT License.
#


def triple_step(stair_count, memorization):
    if stair_count == 1 or stair_count == 0:
        return 1
    elif stair_count == 2:
        return 2

    if memorization[stair_count] is None:
        memorization[stair_count] = triple_step(stair_count - 3, memorization) + triple_step(stair_count - 2, memorization) + triple_step(stair_count - 1, memorization)

    return memorization[stair_count]


stair_count = 100
print(triple_step(stair_count, [None]*(stair_count + 1)))
