#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''
class Solution:
    def totalNQueens(self, n):
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
        return len(result)