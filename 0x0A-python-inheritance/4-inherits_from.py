#!/usr/bin/python3

def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and obj.__class__ is not a_class 
