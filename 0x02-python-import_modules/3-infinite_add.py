#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for numbers in sys.argv[1:]:
        result += int(numbers)
    print(result)
