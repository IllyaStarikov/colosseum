#!/usr/local/bin/python3
#
# counting-valleys.py
# hacker-rank
#
# Created by Illya Starikov on 07/15/19.
# Copyright 2019. Illya Starikov. MIT License.
#


def compliment(step):
    assert step in ["U", "D"]

    return {
        "U": "D",
        "D": "U",
    }[step]


def count_valley(mountain_valleys):
    stack = []
    total_valleys = 0

    for step in mountain_valleys:
        assert step in ["U", "D"]

        if len(stack) == 0:
            stack.append(step)
        elif stack[-1] == compliment(step):
            stack.pop()

            if len(stack) == 0 and step == "U":
                total_valleys += 1
        else:
            stack.append(step)

    return total_valleys


def main():
    input()
    input_ = input()

    print(count_valley(input_))


if __name__ == "__main__":
    main()
