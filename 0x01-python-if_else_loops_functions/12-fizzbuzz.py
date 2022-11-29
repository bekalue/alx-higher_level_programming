#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 is 0:
            print("FizzBuzz", end='')
        elif i % 3 is 0:
            print("Fizz", end='')
        elif i % 5 is 0:
            print("Buzz", end='')
        else:
            print("{}".format(i), end='')
        print(" ", end='')
