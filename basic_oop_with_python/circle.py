#!/usr/bin/python
import math

''' Class Circle '''
class Circle():
    def __init__(self, radius):
        self.__color = []
        self.__center = []
        self.name = []
        self.__radius = radius

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_center(self):
        return self.__center

    def set_center(self, list):
        self.__center = [list[0], list[1]]
                
    def area(self):
        return math.pi * self.__radius ** 2
