#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i + 1, 10):
        if i is not 8:
            print("{}{},".format(i, x), end=' ')
        else:
            print("{}{}".format(i, x))
