#!/usr/bin/python3
"""list of lists representing the pascal triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        pascal.append(list(map(int, list(str(11**i)))))
    return pascal