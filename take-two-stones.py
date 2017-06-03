#!/usr/bin/python

stones = int(input())

if (stones % 4) % 2 == 0:
    print("Bob")
else:
    print("Alice")