#!/usr/local/bin/python3
#
# equalize-the-array.py
# hacker-rank
#
# Created by Illya Starikov on 11/02/19.
# Copyright 2019. Illya Starikov. MIT License.
#

from collections import Counter


def equalize_the_array(list_):
    # To get the number of elements to delete, just find the most
    # common element, and subtract the number of occurences of it
    # from the length of the list
    return len(list_) - Counter(list_).most_common(1)[0][1]


def main():
    _ = input()
    list_ = list(map(int, input().split(' ')))

    count_to_delete = equalize_the_array(list_)
    print(count_to_delete)


if __name__ == "__main__":
    main()
