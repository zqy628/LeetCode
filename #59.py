#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        direction = 0
        i, j = 0, 0
        # if n ==1:
        #     return [1]
        number = 1
        while True:
            cc = direction // 4
            if direction % 4 == 0:
                for j in range(cc, n - cc):
                    if matrix[i][j] == 0:
                        # r.append(matrix[i][j])
                        matrix[i][j] = number
                        number += 1
                    else:
                        break
                if matrix[i + 1][j] != 0:
                    # print('break1')
                    break
            if direction % 4 == 1:
                for i in range(cc + 1, n - cc):
                    if matrix[i][j] == 0:
                        matrix[i][j] = number
                        number += 1
                    else:
                        break
                if matrix[i][j - 1] != 0:
                    # print('break2')
                    break
            if direction % 4 == 2:
                for j in range(n- cc - 2, cc - 1, -1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = number
                        number += 1
                    else:
                        break
                if matrix[i - 1][j] != 0:
                    # print('break3')
                    break
            if direction % 4 == 3:
                for i in range(n - cc - 2, cc , -1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = number
                        number += 1
                    else:
                        break
                if matrix[i][j + 1] != 0:
                    print('break4')
                    break
            # print(matrix)
            direction += 1
        return matrix