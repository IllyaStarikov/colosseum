#!/usr/local/bin/python3
#
# 2d-array-ds.py
# hacker-rank
#
# Created by Illya Starikov on 10/29/19.
# Copyright 2019. Illya Starikov. MIT License.
#


ARRAY_SIZE = 6


def hourglassSum(arr):
    sums = []

    # This is kind of a hack but the most elegant way I could think of
    for row in range(ARRAY_SIZE):
        for column in range(ARRAY_SIZE):
            try:
                sum_ = 0

                sum_ += sum(arr[row + 1][column - 1:column + 2])   # Higher
                sum_ += arr[row][column]                           # Middle
                sum_ += sum(arr[row - 1][column - 1:column + 2])   # Lower

                # Sometimes we get 0 for one of the dimensions and I have no idea why
                if len(arr[row + 1][column - 1:column + 2]) == ARRAY_SIZE // 2  \
                        and len(arr[row - 1][column - 1:column + 2]) == ARRAY_SIZE // 2:
                    sums += [sum_]

            except IndexError:
                pass

    return max(sums)


def get_input():
    """Gets input, hardcoded to expected input"""

    arr = []

    for _ in range(ARRAY_SIZE):
        arr.append(list(map(int, input().rstrip().split())))

    return arr


def main():
    array = get_input()
    max_sum = hourglassSum(array)

    print(max_sum)


if __name__ == "__main__":
    main()
