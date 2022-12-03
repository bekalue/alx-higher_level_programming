#!/usr/bin/python3
def no_c(my_string):
    no_c_string = []
    for i in my_string:
        if i != 'c' and i != 'C':
            no_c_string.append(i)
    return ''.join(no_c_string)
