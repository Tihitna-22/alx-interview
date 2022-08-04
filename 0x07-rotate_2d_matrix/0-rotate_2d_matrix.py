#!/usr/bin/python3
"""
function rotates 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    newmatrics = matrix
    for i in range(len(matrix)):
        for j in range(i):
            temp1 = matrix[i][j]
            temp2 = matrix[j][i]
            newmatrics[i][j] = temp2
            newmatrics[j][i] = temp1
    # print(newmatrics)
    for i in matrix:
        i.reverse()
    # print(matrix)
