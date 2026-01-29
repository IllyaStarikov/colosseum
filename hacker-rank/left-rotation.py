#!/usr/local/bin/python3
#
# left-rotation.py
# hacker-rank
#
# Created by Illya Starikov on 10/30/19.
# Copyright 2019. Illya Starikov. MIT License.
#


def rotate_left(list_, rotations):
    return list_[rotations:] + list_[:rotations]


def main():
    _, rotations = [int(input_) for input_ in input().split()]
    list_ = list(map(int, input().rstrip().split()))

    result = rotate_left(list_, rotations)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
