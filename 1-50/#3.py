#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


#滑动窗口法
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        slen = len(s)
        substring = 0
        for i in range(slen):
            if s[i] in l:
                j = l.index(s[i])
                l = l[j+1:]
            l.append(s[i])
            if len(l) > substring:
                substring = len(l)
        return substring
s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
