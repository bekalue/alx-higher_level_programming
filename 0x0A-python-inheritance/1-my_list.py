#!/usr/bin/python3
"""
A module containing a list subclass.
"""


class MyList(list):
    """
    A list subclass.
    """

    def print_sorted(self):
        """
        Prints this list in a sorted order.
        """
        print(sorted(self))
