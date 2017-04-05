#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Code by Héctor Blanco Lozano

import sys
from copy import deepcopy


class Matrix(object):

    def __init__(self, *args):
        if len(args[0]) == 2 and len(args[0][0]) == 2:
            self.coordinates_vector = []
            self.coordinates_vector = [(0, 0), (0, 1), (1, 0), (1, 1)]
            self.rows = args[0]
            self.nrows = len(self.rows)
            self.ncols = len(self.rows[0])
        else:
            sys.exit('Error: ¡The dimension of the matrices must be 2x2!')

    def __add__(self, op1):
        if type(op1) == type(self):  # Matrix + Matrix
            result = deepcopy(self)
            for tuple in self.coordinates_vector:
                result.rows[tuple[0]][tuple[1]] += op1.rows[tuple[0]][tuple[1]]
            return result
        else:  # Matrix + Scalar
            try:
                result = deepcopy(self)
                for tuple in self.coordinates_vector:
                    result.rows[tuple[0]][tuple[1]] += op1
            except TypeError:
                sys.exit('Error: Operands are not valid. They must be matrix'
                         '(2x2) or scalar')
            return result

    def __sub__(self, op1):
        if type(op1) == type(self):  # Matrix + Matrix
            result = deepcopy(self)
            for tuple in self.coordinates_vector:
                result.rows[tuple[0]][tuple[1]] -= op1.rows[tuple[0]][tuple[1]]
            return result
        else:  # Matrix + Scalar
            try:
                result = deepcopy(self)
                for tuple in self.coordinates_vector:
                    result.rows[tuple[0]][tuple[1]] -= op1
            except TypeError:
                sys.exit('Error: Operands are not valid. They must be matrix'
                         ' (2x2) or scalar')
            return result

    def prod(self, op1):
        C = [[0 for row in range(op1.ncols)] for col in range(self.nrows)]
        for i in range(self.nrows):
            for j in range(op1.ncols):
                for k in range(op1.nrows):
                    C[i][j] += self.rows[i][k] * op1.rows[k][j]
        result = Matrix(C)
        return result

    def __iter__(self):
        return iter(self.rows)

    def __str__(self):
        matrix_str = '|'
        i = 0
        for tuple in self.coordinates_vector:
            matrix_str += ' '
            if tuple[0] == 0:
                matrix_str += str(self.rows[tuple[0]][tuple[1]])
            elif i == 0:
                matrix_str += '|\n| ' + str(self.rows[tuple[0]][tuple[1]])
                i = 1
            elif i == 1:
                matrix_str += str(self.rows[tuple[0]][tuple[1]]) + ' |\n'
        return matrix_str
