#!/usr/bin/python3
"""This module contains a peak-finding function"""


def find_peak(list_of_integers):
    """Return a peak(maximum) in a list of unsorted integrs"""
    if list_of_integers == []:
        return None

    size = len(lilst_of_integers)
    if size == 1:
        return list_ofintegers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    elif peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    else:
        return find_peak(list_of_integers[mid + 1:])
