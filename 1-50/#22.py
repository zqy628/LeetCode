#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
import itertools
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #先遍历出所有()*n的排列，再筛选
        #时间复杂度太高
        str = '()' * n
        l = []
        for i in itertools.permutations(str,len(str)):
            if self.isParentheses(''.join(list(i))):
                l.append(''.join(list(i)))
        return list(set(l))

    def isParentheses(self, s):
        lenth = len(s)
        l = []
        for i in range(lenth):
            if s[i] == '(':
                l.append(s[i])
            elif s[i] == ')':
                if l != [] and '(' == l[-1]:
                    l.pop()
                else:
                    return False
        return l == []

    def generateParenthesis1(self, n):
        #递归插入()
        if n == 1:
            l = ['()']
            return l
        l_ = []
        for i in self.generateParenthesis1(n-1): #list内循环
            for j in range(len(i)+1):
                l_.append(i[:j] + '()' + i[j:])
        l = list(set(l_))
        return l

s = Solution()
print(s.generateParenthesis1(5))