#!/usr/bin/python3
def roman_to_int(roman_string):
    a_dictionary = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    prev, summ = 0, 0

    for x in roman_string:
        summ += a_dictionary[x] if a_dictionary[x] <= prev else a_dictionary[x] - prev * 2
        prev = a_dictionary[x]
    return summ
