#!/usr/bin/python3
"""Contains classes for working with Polygons.
"""
import os
import re
from random import randint
from json import JSONDecoder, JSONEncoder
from turtle import Pen


class Base:
    """Represents the base class for all polygon objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new polygon object with the given id.

        Args:
            id (int): The id of this polygon object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Creates the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return JSONEncoder().encode(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of polygons to a file in JSON format.

        Args:
            list_objs (list): A list of polygons.
        """
        file_name = '{}.json'.format(cls.__name__)
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                if type(obj) is cls:
                    dict_list.append(obj.to_dictionary())
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Creates a list from its JSON representation.

        Args:
            json_string (str): A JSON string representation of a list.

        Returns:
            list: A JSON representation of the list of dictionaries.
        """
        if (json_string is None) or (len(json_string.strip()) == 0):
            return []
        else:
            return JSONDecoder().decode(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a polygon with the given attributes.

        Args:
            dictionary (dict): A dictionary of the object's attributes.

        Returns:
            Base: A polygon object with the given attributes.
        """
        polygons = {
            'Rectangle': (1, 1, 0, 0, None),
            'Square': (1, 0, 0, None),
        }
        if cls.__name__ in polygons.keys():
            polygon = cls(*polygons[cls.__name__])
            polygon.update(**dictionary)
            return polygon

    @classmethod
    def load_from_file(cls):
        """Loads a list of polygons from a file in JSON format.

        Returns:
            list: A list of polygons.
        """
        file_name = '{}.json'.format(cls.__name__)
        lines = []
        if os.path.isfile(file_name):
            with open(file_name, mode='r') as file:
                for line in file.readlines():
                    lines.append(line)
        txt = ''.join(lines)
        attr_dicts = cls.from_json_string(txt)
        cls_list = list(map(lambda x: cls.create(**x), attr_dicts))
        return cls_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of polygons to a file in CSV format.

        Args:
            list_objs (list): A list of polygons.
        """
        file_name = '{}.csv'.format(cls.__name__)
        poly_fmt_fxns = {
            'Rectangle': lambda x: '{},{:d},{:d},{:d},{:d}'.format(
                x.id, x.width, x.height, x.x, x.y),
            'Square': lambda x: '{},{:d},{:d},{:d}'.format(
                x.id, x.size, x.x, x.y),
        }
        vals_list = []
        if list_objs is not None:
            poly_name = cls.__name__
            for obj in list_objs:
                if (type(obj) is cls) and (poly_name in poly_fmt_fxns):
                    vals_list.append('{}\n'.format(
                        poly_fmt_fxns[poly_name](obj)))
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.writelines(vals_list)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of polygons from a file in CSV format.

        Returns:
            list: A list of polygons.
        """
        poly_name = cls.__name__
        file_name = '{}.csv'.format(poly_name)
        poly_fmt_fxns = {
            'Rectangle': lambda x: {
                'id': int(x[0]),
                'width': int(x[1]),
                'height': int(x[2]),
                'x': int(x[3]),
                'y': int(x[4]),
            },
            'Square': lambda x: {
                'id': int(x[0]),
                'size': int(x[1]),
                'x': int(x[2]),
                'y': int(x[3]),
            },
        }
        poly_fmt = {
            'Rectangle': r'\s*[^,]+,[^,]+,[^,]+,[^,]+,[^,]+',
            'Square': r'\s*[^,]+,[^,]+,[^,]+,[^,]+',
        }
        lines = []
        attr_dicts = []
        if os.path.isfile(file_name):
            with open(file_name, mode='r') as file:
                for line in file.readlines():
                    attrs_match = re.match(poly_fmt[poly_name], line)
                    if attrs_match is not None:
                        cols = line.strip().split(',')
                        attr_dicts.append(poly_fmt_fxns[poly_name](cols))
        cls_list = list(map(lambda x: cls.create(**x), attr_dicts))
        return cls_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the polygons in each list using Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle objects.
            list_squares (list): A list of Square objects.
        """
        poly_list = []
        funcs = {
            'hex_to_rgb': lambda x: (x >> 16, (x >> 8) % 0xff, x % 0xff)
        }
        pen = Pen()
        screen = pen.getscreen()
        poly_list.extend(list_rectangles)
        poly_list.extend(list_squares)
        wind_width = max(
            [max(map(lambda x: x.width + x.x, poly_list)) + 4, 460.8])
        wind_height = max(
            [max(map(lambda x: x.height + x.y, poly_list)) + 4, 259.2])
        screen.setup(width=wind_width, height=wind_height)
        screen.setworldcoordinates(0, wind_height, wind_width, 0)
        pen.speed('slowest')
        pen.degrees()
        pen.pensize(2)
        pen.hideturtle()
        for i in range(len(poly_list)):
            rect = poly_list[i]
            pen.up()
            pen.forward(rect.x)
            pen.right(90)
            pen.backward(rect.y)
            pen.showturtle()
            pen.down()
            pen.begin_poly()
            pen.fillcolor(funcs['hex_to_rgb'](randint(0, 0xffffff)))
            pen.pencolor(funcs['hex_to_rgb'](randint(0, 0xffffff)))
            pen.begin_fill()
            pen.backward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.backward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.end_fill()
            pen.end_poly()
            pen.up()
            # move to start pos
            pen.hideturtle()
            pen.right(90)
            pen.backward(rect.y)
            pen.left(90)
            pen.forward(rect.x)
            pen.right(180)
        while True:
            c = input('Enter "q" to quit: ')
            if c == 'q':
                break
