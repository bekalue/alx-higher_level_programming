#!/usr/bin/python3
'''A module containing a rebellious int.
'''


class MyInt(int):
    '''Represents a rebellious integer object.
    '''
    def __eq__(self, other):
        '''Checks if the given value is not equal to the
        value of this object.

        Args:
            other (MyInt): The value to be compared against.

        Returns:
            bool: True if the value is not equal to the value
            stored by this object.
        '''
        return super().__ne__(other)

    def __ne__(self, other):
        '''Checks if the given value is equal to the value
        of this object.

        Args:
            other (MyInt): The value to be compared against.

        Returns:
            bool: True if the value is equal to the value
            stored by this object.
        '''
        return super().__eq__(other)
