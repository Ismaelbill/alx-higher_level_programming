#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv[1:])
    arguments = sys.argv[1:]
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(arguments[0]))
    elif length > 1:
        print("{} arguments:".format(length))
        num = 1
        for i in arguments:
            print("{:d}: {}".format(num, i))
            num += 1
