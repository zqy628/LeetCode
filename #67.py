#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = str(int(a) + int(b))
        c = list(c)
        c = [int(i) for i in c]
        for i in range(1,len(c))[::-1]:
            if c[i] >= 2:
                c[i] = c[i] - 2
                c[i-1] += 1
        if c[0] >= 2:
            c[0] = c[0] - 2
            c = [1] + c
        return ''.join([str(i) for i in c])