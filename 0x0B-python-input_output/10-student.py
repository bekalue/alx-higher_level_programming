#!/usr/bin/python3
'''A module for managing students.
'''


class Student:
    '''Represents a student.
    '''
    def __init__(self, first_name, last_name, age):
        '''Initializes this student with the given first name,
        last name, and age.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary of this student's attributes.

        Args:
            attrs (list): A list of attributes that can be retrieved.

        Returns:
            dict: A dictionary of this student's attributes.
        '''
        if '__dict__' in dir(self):
            res = dict()
            can_filter = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                can_filter = True
            for key in self.__dict__.keys():
                if (not can_filter) or (can_filter and key in attrs):
                    res[key] = self.__dict__[key]
            return res
