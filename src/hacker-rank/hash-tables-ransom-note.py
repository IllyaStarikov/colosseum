#!/usr/local/bin/python3
#
# hash-tables-ransom-note.py
# hacker-rank
#
# Created by Illya Starikov on 11/03/19.
# Copyright 2019. Illya Starikov. MIT License.
#

from collections import defaultdict


def ransom_note(magazine, ransom_note):
    words_used = defaultdict(int)

    ransom_note_list = ransom_note.split(' ')
    magazine_list = magazine.split(' ')

    # build the dict, so we can't use words more than once :)
    for word in magazine_list:
        words_used[word] += 1

    for word in ransom_note_list:
        if words_used[word] == 0:
            return "No"

        words_used[word] -= 1

    return "Yes"


def main():
    _ = input()
    magazine = input()
    ransom = input()

    result = ransom_note(magazine, ransom)

    print(result)


if __name__ == "__main__":
    main()
