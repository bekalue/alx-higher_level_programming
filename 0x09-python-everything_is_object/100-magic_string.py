#!/usr/bin/python3
def magic_string():
    magic_string.c, t = (magic_string.__dict__.get('c', 0) + 1, ', BestSchool')
    return '{:s}{:s}'.format(t[2:], t * (magic_string.c - 1))
