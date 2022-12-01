#!/usr/bin/python3
import calculator_1 as calc

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, int(calc.div(a, b))))
