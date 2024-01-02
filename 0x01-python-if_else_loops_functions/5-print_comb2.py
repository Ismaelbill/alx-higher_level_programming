#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(i)
        break
    print(f"0{i}, " if i < 10 else f"{i}, ", end="")
