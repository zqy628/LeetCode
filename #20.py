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
        l = []
        for i in range(lenth):
            if s[i] in dic.values():
                l.append(s[i])
            elif s[i] in dic.keys():
                if l != [] and dic[s[i]] == l[-1]:
                    l.pop()
                else:
                    return False
        return l == []

s = Solution()
print(s.isValid('['))