#!/usr/bin/python3
""" module for Base class """

import json
import os
import turtle


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not None, assign the public instance attribute id
        with this argument value - you can assume id is an integer
        and you don’t need to test the type of it
        otherwise, increment __nb_objects and assign the new value
        to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        a = "{}.json".format(cls.__name__)
        with open(a, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        n = []
        if json_string is not None or json_string != '':
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")
            n = json.loads(json_string)
        return n

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            instance = cls(width=1, height=1)
        elif cls.__name__ == 'Square':
            instance = cls(size=1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        a = "{}.json".format(cls.__name__)
        instance_list = []
        dictionary_list = []

        if os.path.exists(a):
            with open(a, "r") as f:
                my_str = f.read()
                dictionary_list = cls.from_json_string(my_str)
                for i in dictionary_list:
                    instance_list.append(cls.create(**i))
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
