#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        l = [1 for i in range(n)]
        for i in range(n):
            if obstacleGrid[m-1][n-i-1] == 1:
                l[i:] = [0 for j in range(n-i)]
                break
        print (l)
        # for i in range(m):
        #     if obstacleGrid[m][n-1] != 1:
        #         obstacleGrid[m][n - 1] = 1
        i = 1
        while i < m:
            if obstacleGrid[m-1-i][n-1] == 1:
                l[0] = 0
            for j in range(1,n):
                if obstacleGrid[m-1-i][n-1-j] == 1:
                    l[j] = 0
                else:
                    l[j] = l[j-1] + l[j]
            print (l)
            i += 1
        return l[-1]