#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle:
            if needle in haystack:
                for i in range(len(haystack)-len(needle)+1):
                    for j in range(len(needle)):
                        if haystack[i+j] != needle[j]:
                            break
                    if j == len(needle)-1 and haystack[i+j] == needle[j]:
                        return i
            else:
                return -1
        else:
            return 0