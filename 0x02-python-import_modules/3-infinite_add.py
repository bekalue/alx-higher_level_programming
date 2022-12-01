#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("0")
        exit()
    it = 0
    for numbers in sys.argv:
        if it == 1:
            continue
        result += int(numbers)
    print(result)
