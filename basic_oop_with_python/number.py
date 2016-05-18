#!/usr/bin/python
import math

"""Class"""
class Number(object):
    """Constructs a number."""
    def __init__(self, value):
        self.__value = value

    def set_value(self, sum):
        self.__value = sum

    def get_value(self):
        return self.__value

    """Redefine operators."""
    def __add__(self,other):
        return Number(self.__value + other.__value)

    def __sub__(self,other):
        return Number(self.__value - other.__value)

    def __mul__(self,other):
        return Number(self.__value * other.__value)

    def __div__(self,other):
        return Number(self.__value / other.__value)

    def __str__(self):
        return str(self.__value)
