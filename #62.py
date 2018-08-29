#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''
#每一个格子的路径数为下方和右方路径数之和
#Time Limit Exceeded
class Solution1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1 for i in range(m)]
        i = 1
        while i < n:
            for j in range(1,m):
                l[j] = l[j-1] + l[j]
            i += 1
        return l[-1]
s = Solution()
print(s.uniquePaths(23,12))