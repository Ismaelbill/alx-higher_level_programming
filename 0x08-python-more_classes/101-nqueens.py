#!/usr/bin/python3
""" N queens """


import sys
args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

if not isinstance(int(args[1]), int):
    print("N must be a number")
    exit(1)

arg = int(args[1])

if arg < 4:
    print("N must be at least 4")
    exit(1)

print(arg)
