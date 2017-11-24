#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')':'(','}':'{',']':'['}
        lenth = len(s)
        i = 0
        l = []
        while i < lenth:
            if s[i] in ['(','[','{']:
                l.append(s[i])