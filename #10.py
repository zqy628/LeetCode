#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''
#很难啊。。。
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if '*' in p:
            while True:
                if s[0] != p[0] and p[0] != '.':
                    if p[1] == '*':
                        p = p[2:]
                    else:
                        return False
                else:
                    if s[1] == s[0] and p[1] == '*':
                        pass


        elif '.' in p:
            if len(s) == len(p):
                for i in range(len(s)):
                    if s[i] == p[i] or p[i] == '.':
                        pass
                    else:
                        return False
                return True
            else:
                return False
        else:
            return s == p
#Approach #1: Recursion [Accepted] 递归,不符合时间复杂度
    def isMatch1(self, s, p):
        #判断两者是否都为空
        if not p:
            return not s
        #首先判断第一个字符是否匹配
        first_match = bool(s) and p[0] in [s[0],'.']
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch1(s,p[2:]) or first_match and self.isMatch1(s[1:],p) #'与'优先级比'或'高
        else:
            return first_match and self.isMatch1(s[1:],p[1:])

#Approach  # 2: Dynamic Programming [Accepted]
#除了调用match(text[i:], pattern[j:])，我们使用dp(i, j)来处理这些调用，节省了我们昂贵的字符串构建操作，并允许我们缓存中间结果。
#动态规划最优子结构
    def isMatch2(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

#Bottom-Up Variation 设置一个二维数组，难以理解
    def isMatch3(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        print(dp)
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

s = Solution()
s.isMatch3("aab", "c*a*b")