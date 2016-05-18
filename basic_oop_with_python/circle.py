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

    def intersection(self, c_bis):
        '''sum of the radii'''
        sum_radii = self.__radius + c_bis.__radius

        delta_x = c_bis.get_center()[0] - self.get_center()[0]
        delta_y = c_bis.get_center()[1] - self.get_center()[1]

        ''' if r^2 < a^2 + b^2 '''
        ''' they do not intersect '''
        if (sum_radii ** 2 < delta_x ** 2 + delta_y ** 2):
            return 0
        
        ''' otherwise '''
        ''' they intersect '''
        return 1

    def intersection_percentage(self, c_bis):

        delta_x = c_bis.get_center()[0] - self.get_center()[0]
        delta_y = c_bis.get_center()[1] - self.get_center()[1]
        r = self.__radius
        R = c_bis.__radius

        ''' r2 and R2 are the square of the radius '''
        r2 = r ** 2
        R2 = R ** 2

        ''' distance squared between the centers '''
        d2 = delta_x ** 2 + delta_y ** 2
        ''' distance between the centers '''
        d = math.sqrt(delta_x ** 2 + delta_y ** 2)

        area = r2 * math.acos((d2 + r2 - R2)/(2 * d * r)) + R2 * math.acos((d2 + R2 - r2)/(2 * d * R)) - (.5) * math.sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R))
        
        return  ((area / (math.pi * r2)) * 100)
