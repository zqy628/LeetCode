#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ['1']
        for i in range(n - 1):
            s_ = ''
            start = 0
            count = 0
            for j in range(len(s[-1])):
                if s[-1][j] == s[-1][start]:
                    count += 1
                else:
                    s_ = s_ + str(count) + str(s[-1][start])
                    start = j+1
                    count = 0
            s.append(s_)
        return s[-1]
