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

    #Approach3 (Dynamic Programming) [Accepted]
    def longestPalindrome2(self, s):
        lenth = len(s)
        substring = []
        #eg:bbc
        if lenth >= 2:
            if s[0] == s[1]:
                substring.append(s[:2])
        #单个字符两边遍历  eg: aba
        for i in range(1,lenth):
            j = i
            while i>=1 and j<=lenth-2:
                (i,j) = (i-1,j+1)
                if s[i] == s[j]:
                    substring.append(s[i:j+1])
                else:
                    break
        #双字符两边遍历  eg: abba
        for i in range(1,lenth-1):
            j = i+1
            if s[i] == s[j]:
                substring.append(s[i:j+1])
                while i>=1 and j<=lenth-2:
                    (i,j) = (i-1,j+1)
                    if s[i] == s[j]:
                        substring.append(s[i:j+1])
                    else:
                        break
        if substring == []:
            sub = s[0]
        else:
            sub = sorted(substring, key=lambda x: len(x))[-1]
        return sub

    #Approach #4 (Expand Around Center) [Accepted]
    def longestPalindrome3(self, s):
        lenth = len(s)
        start = 0
        end = 0
        for i in range(lenth):
            len1 = Solution.expandAroundCenter(s, i, i)
            len2 = Solution.expandAroundCenter(s, i, i + 1)
            len_ = max(len1, len2)
            if (len_ > end - start):
                start = i - (len_ - 1) // 2
                end = i + len_ // 2
        return s[start:end + 1]

    def expandAroundCenter(s, left, right):
        lenth = len(s)
        L = left
        R = right
        while L >= 0 and R < lenth and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    #Approach #5 (Manacher's Algorithm) [Accepted]
    #思想：在每个字符左右都加上一个特殊字符，比如加上'#'，那么处理后字符串都为奇数
    #从而不必分类讨论，时间复杂度降为O(n)


s = Solution()
print(s.longestPalindrome3('ccd'))