#!/usr/local/bin/python3
#
# stock-merchant.py
# hacker-rank
#
# Created by Illya Starikov on 07/15/19.
# Copyright 2019. Illya Starikov. MIT License.
#


def number_of_pairs(total_socks):
    return total_socks // 2


def match_socks(socks):
    match = {}

    for sock in socks:
        if sock not in match.keys():
            match[sock] = 0

        match[sock] += 1

    total = 0

    for _, total_socks_per_color in match.items():
        total += number_of_pairs(total_socks_per_color)

    return total
