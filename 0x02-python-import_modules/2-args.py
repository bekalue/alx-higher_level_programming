#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
        exit()
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    i = 0
    for word in sys.argv:
        i += 1
        if i == 1:
            continue
        print("{}: {}".format(i, word))
