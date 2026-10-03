#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        triangle = []
        return triangle

    triangle = [[1]] # default row built if n is <= 0
    while len(triangle) != n:
        prev_row = triangle[-1] # the last row added
        new_row = [1] # every row starts with 1
        for i in range(1, len(prev_row)): # middle positions only
            new_row.append(prev_row[i-1] + prev_row[i])
        new_row.append(1) # every row ends wih 1
        triangle.append(new_row) # add newly created row to triangle
    return triangle
