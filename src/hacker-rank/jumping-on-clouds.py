#!/usr/local/bin/python3
#
# jumping-on-clouds.py
# hacker-rank
#
# Copyright 2019. Illya Starikov. MIT License.
# Created by Illya Starikov on 07/15/19.
#


def jump_on_clouds(formation):
    formation = formation.split(' ')

    length = len(formation) - 1  # zero indexed length
    jump_count = 0
    i = 0

    # although we don't enumerate the entire length 1...N,
    # we have a case where if i hits length - 1 it will terminate
    while i < length - 2:
        if formation[i + 2] == "0":
            i += 2
        elif formation[i + 1] == "0":
            i += 1
        else:
            raise Exception

        jump_count += 1

    if i != length:
        jump_count += 1

    return jump_count


input()
input_ = input()

print(jump_on_clouds(input_))
