#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''
# Time Limit Exceeded (Brute Force
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        subs = []
        for i in range(l-1):
            for j in range(i+1,l):
                subs.append(s[i:j+1])
        # print(subs)
        lenth = []
        for string in subs:
            count = 0
            Flag = True
            for char in string:
                if char == '(':
                    count += 1
                else:
                    if count == 0:
                        Flag = False
                        break
                    else:
                        count -= 1
            if count == 0 and Flag:
                lenth.append(len(string))
        if lenth:
            return max(lenth)
        else:
            return 0

#https://leetcode.com/problems/longest-valid-parentheses/solution/
#2 Using Dynamic Programming [Accepted]
class Solution1:
    def longestValidParentheses(self, s):
        l = len(s)
        if l <= 1:
            return 0
        pos = [0 for i in range(l)]
        for i in range(1,l):
            if s[i] == ')' and s[i-1] == '(':
                if i-2 >= 0:
                    pos[i] = pos[i-2] + 2
                else:pos[i] = 2
            elif s[i] == ')' and s[i-1] == ')':
                if i-pos[i-1]-1>=0:
                    if s[i-pos[i-1]-1] == '(':
                        pos[i] = pos[i-1] + pos[i-pos[i-1]-2] + 2
        return max(pos)

#3 Using Stack [Accepted] (The Best)
class Solution2:
    def longestValidParentheses(self, s):
        stack = [-1]
        m = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    m = max(m,i-stack[-1])
                #key point
                else:
                    stack.append(i)
        return m