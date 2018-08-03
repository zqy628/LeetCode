#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        matrix_nums = [[['9', '1', '2', '3', '4', '5', '6', '7', '8'] for i in range(9)] for i in range(9)]
        nums = ['9', '1', '2', '3', '4', '5', '6', '7', '8']
        for i in range(9):
            for j in range(9):
                if board[i][j] in nums:
                    matrix_nums[i][j] = []
                    # print(matrix_nums)
                elif board[i][j] == '.':
                    # nums_ = nums
                    for m in range(9):
                        if board[i][m] in matrix_nums[i][j]:
                            matrix_nums[i][j].remove(board[i][m])
                        if board[m][j] in matrix_nums[i][j]:
                            matrix_nums[i][j].remove(board[m][j])
                    m, n = i // 3, j // 3
                    for u in range(m, m + 3):
                        for v in range(n, n + 3):
                            if board[u][v] in matrix_nums[i][j]:
                                matrix_nums[i][j].remove(board[u][v])
        print(matrix_nums)
        flag = True
        flag1 = True
        while flag:
            flag = False
            if flag1:
                flag1 = False
                for i in range(9):
                    for j in range(9):
                        if len(matrix_nums[i][j]) == 1:
                            # print("ture")
                            board[i][j] = matrix_nums[i][j][0]
                            matrix_nums[i][j].remove(matrix_nums[i][j][0])
                            for m in range(9):
                                if board[i][j] in matrix_nums[i][m]:
                                    matrix_nums[i][m].remove(board[i][j])
                                if board[i][j] in matrix_nums[m][j]:
                                    matrix_nums[m][j].remove(board[i][j])
                            m, n = i // 3, j // 3
                            for u in range(m, m + 3):
                                for v in range(n, n + 3):
                                    if board[i][j] in matrix_nums[u][v]:
                                        matrix_nums[u][v].remove(board[i][j])
            else:
                flag1 = False
                for i in range(9):
                    for j in range(9):
                        if len(matrix_nums[i][j]) >= 2:
                            # print("ture")
                            board[i][j] = matrix_nums[i][j][0]
                            matrix_nums[i][j].remove(matrix_nums[i][j][0])
                            for m in range(9):
                                if board[i][j] in matrix_nums[i][m]:
                                    matrix_nums[i][m].remove(board[i][j])
                                if board[i][j] in matrix_nums[m][j]:
                                    matrix_nums[m][j].remove(board[i][j])
                            m, n = i // 3, j // 3
                            for u in range(m, m + 3):
                                for v in range(n, n + 3):
                                    if board[i][j] in matrix_nums[u][v]:
                                        matrix_nums[u][v].remove(board[i][j])

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        flag = True
                    if len(matrix_nums[i][j]) == 1:
                        flag1 = True
            print(matrix_nums)
            print(board)
s = Solution()
print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))





