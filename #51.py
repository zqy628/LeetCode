#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''
#DFS动态规划
#In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) where p + q == x + y or p - q == x - y would be invalid.
# We can use this information to keep track of the indicators (xy_dif and xy_sum ) of the invalid positions and then call DFS recursively with valid positions only.
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens,q_dif,q_sum):
            l = len(queens)
            if l == n:
                result.append(queens)
            for q in range(n):
                if q not in queens and q-l not in q_dif and q+l not in q_sum:
                    DFS(queens+[q],q_dif+[q-l],q_sum+[q+l])
        result = []
        DFS([],[],[])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
