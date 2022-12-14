#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_max_integer(unittest.TestCase):
    """
    a class that ineherits TestCase class for testing.
    """

    def test_max_integer(self):
        """
        the method tests max_integer function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, 3, 43, -97, 50, 13]), 50)
        self.assertEqual(max_integer([5, 12, -12, 12, -12]), 12)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([7, 2, -3, 45, 6]), 45)
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)
        self.assertEqual(max_integer([-7, 1, -18, -6]), 1)
        self.assertEqual(max_integer([7, 1, -18, -6]), 7)
        self.assertEqual(max_integer([-7, 1, -18, 9]), 9)

if __name__ == "__main__":
    unittest.main()
