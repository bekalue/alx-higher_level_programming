#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed = my_list.reverse()
    for i in reversed:
        print("{:d}".format(i))
