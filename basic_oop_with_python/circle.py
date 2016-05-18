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

        ''' center distance with respect to x-axis and y-axis '''
        delta_x = c_bis.get_center()[0] - self.get_center()[0]
        delta_y = c_bis.get_center()[1] - self.get_center()[1]

        ''' if (r+R)^2 < a^2 + b^2 '''
        ''' they do not overlap '''
        if (sum_radii ** 2 < delta_x ** 2 + delta_y ** 2):
            return 0
        
        ''' otherwise '''
        ''' they overlap '''
        return 1

    def intersection_percentage(self, c_bis):
        ''' case 1: '''
        ''' if they do not overlap '''
        ''' return 0 percent '''
        if (self.intersection(c_bis) == 0):
            return 0

        ''' center distance with respect to x-axis and y-axis '''
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

        ''' case 2: '''
        ''' if they are points '''
        if (r == 0 and R == 0 and d == 0):
            ''' if they are the same point '''
            ''' return 100% '''
            return 100
        elif (r == 0 and R == 0):
            ''' if they are different points '''
            ''' return 0% '''
            return 0;

        ''' case 3: '''
        ''' if they are concentric and r > R '''
        ''' return R2/r2 %'''
        ''' if they are concentric and r <= R '''
        ''' return 100% '''
        if (d == 0 and r > R):
            return (1.) * R2/r2 * 100.
        elif (d == 0):
            return 100;

        ''' case 4: '''
        ''' if one is inside the other and they do not kiss '''
        ''' return R2 / r2 % '''
        ''' if other is larger '''
        ''' return 100% '''
        if (d + R < r):
            return (1.) * R2 / r2 * 100.
        elif (d + r < R):
            return 100

        area = r2 * math.acos((d2 + r2 - R2)/(2 * d * r)) + R2 * math.acos((d2 + R2 - r2)/(2 * d * R)) - (1./2) * math.sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R))
        
        return  ((area / (math.pi * r2)) * 100)
