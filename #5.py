#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''
class Solution:
    #不符合时间复杂度
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenth = len(s)
        maxl = 0
        substring = ''
        for i in range(lenth):
            for j in range(i+1,lenth):
                if j + 1 - i > maxl:
                    l = s[i:j+1]
                    if l == l[::-1]:
                        maxl = j+1-i
                        substring = s[i:j+1]
        if substring == '':
            substring = s[0]
        return substring

    #超出时间限制
    def longestPalindrome1(self, s):
        lenth = len(s)
        maxl = 0
        substring = ''
        s_ = s[::-1]
        print(s_)
        for i in range(lenth):
            for j in range(i+1,lenth):
                if j + 1 - i > maxl:
                    if s_[i:j+1] in s[lenth-1-j:lenth-i]:
                        maxl = j+1-i
                        substring = s_[i:j+1]
        if substring == '':
            substring = s[0]
        return substring

    def longestPalindrome2(self, s):
        lenth = len(s)
        maxl = 0
        substring = ''

s = Solution()
print(s.longestPalindrome1('abcd24314dcba'))