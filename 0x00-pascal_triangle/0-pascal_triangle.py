#!/usr/bin/python3
'''
    list of lists representing the pascal triangle
'''


def pascal_triangle(n):
    '''
        returns a list of lists
    '''
    pascal = []
    if type(n) is not int or n <= 0:
        return []

    for i in range(n):
        pascal.append(list(map(int, list(str(11**i)))))

    return pascal
