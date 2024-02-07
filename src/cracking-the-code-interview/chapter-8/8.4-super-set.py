#!/usr/local/bin/python3
#
# 8.4-super-set.py
# chapter-8
#
# Created by Illya Starikov on 07/24/19.
# Copyright 2019. Illya Starikov. MIT License.
#


def super_set(set_, super_set_list=[], placeholder_set=[]):
    if len(set_) <= 1:
        super_set_list.append(set_)
        return super_set_list
    else:
        set_ = set_
        placeholder_set = placeholder_set

        popped = set_.pop()
        placeholder_set.append(popped)

        super_set_list += [set_, placeholder_set]
        return super_set(set_, super_set_list, placeholder_set)


import pprint
pprint.pprint(super_set([0, 1, 2], []))
