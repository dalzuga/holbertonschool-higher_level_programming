#!/usr/bin/python
''' Returns 1 if odd, 0 if even '''
def odd(x):
    if type(x) is not int:
        return 0

    if (x % 2 == 1):
        return 1
    else:
        return 0
