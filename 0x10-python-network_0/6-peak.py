#!/usr/bin/python3
"""This module contains a peak-finding function"""


def find_peak(list_of_integers):
    """Return a peak(maximum) in a list of unsorted integrs"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
