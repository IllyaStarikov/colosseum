#!/usr/local/bin/python3
#
# deduplicating-files.py
# Desktop
#
# Created by Illya Starikov on 06/10/17.
# Copyright 2017. Illya Starikov. All rights reserved.
#


def hash_function(string):
    _hash = 0
    for character in string:
        _hash ^= ord(character)

    return _hash


lines = int(input())
while lines != 0:
    file_system = {}

    for i in range(0, lines):
        _file = input()
        _hash = hash_function(_file)

        if _hash not in file_system:
            file_system[_hash] = [0, {}]
        file_system[_hash][0] += 1
        if _file not in file_system[_hash][1]:
            file_system[_hash][1][_file] = 1
        else:
            file_system[_hash][1][_file] += 1

    collisions = 0
    files = 0

    for _, val in file_system.items():
        if val[0] > 1:
            for k, v in val[1].items():
                collisions += (val[0] - v) * v
            files += len(val[1])
        else:
            files += 1

    print("{:d} {:d}".format(files, collisions // 2))
    lines = int(input())
