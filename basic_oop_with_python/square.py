#!/usr/bin/python
import math

''' Class Circle '''
class Square():
    def __init__(self, side_length):
        self.__color = []
        self.__center = []
        self.name = []
        self.__side_length = side_length

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_center(self):
        return self.__center

    def set_center(self, list):
        self.__center = [list[0], list[1]]
                
    def area(self):
        return self.__side_length ** 2

    def __str__(self):
        str = ""

        '''print first row'''
        for i in range(0, self.__side_length):
            str+="*"

        ''' print a new line '''
        str+="\n"

        ''' print middle rows '''
        for i in range(0, self.__side_length - 2):

            ''' print the first character '''
            str+="*"

            ''' print the spaces in the middle '''
            for j in range(0, self.__side_length - 2):
                str+=" "

            ''' print the last character and add new line '''
            str+="*\n"

        '''print last row'''
        for i in range(0, self.__side_length):
            str+="*"

        return str
