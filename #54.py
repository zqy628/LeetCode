#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # m_ = matrix
        if matrix == []:
            return []
        direction = 0
        r = []
        i, j = 0, 0
        row, column = len(matrix), len(matrix[0])
        if row ==1:
            return matrix[0]
        while True:
            cc = direction // 4
            if direction % 4 == 0:
                for j in range(cc, column - cc):
                    if matrix[i][j] != -100:
                        r.append(matrix[i][j])
                        matrix[i][j] = -100
                    else:
                        break
                if matrix[i + 1][j] == -100:
                    print('break1')
                    break
            if direction % 4 == 1:
                for i in range(cc + 1, row - cc):
                    if matrix[i][j] != -100:
                        r.append(matrix[i][j])
                        matrix[i][j] = -100
                    else:
                        break
                if matrix[i][j - 1] == -100:
                    print('break2')
                    break
            if direction % 4 == 2:
                for j in range(column- cc - 2, cc - 1, -1):
                    if matrix[i][j] != -100:
                        r.append(matrix[i][j])
                        matrix[i][j] = -100
                    else:
                        break
                if matrix[i - 1][j] == -100:
                    print('break3')
                    break
            if direction % 4 == 3:
                for i in range(row - cc - 2, cc , -1):
                    if matrix[i][j] != -100:
                        r.append(matrix[i][j])
                        matrix[i][j] = -100
                    else:
                        break
                if matrix[i][j + 1] == -100:
                    print('break4')
                    break

            print(matrix)
            direction += 1
        return r