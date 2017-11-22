#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
九宫格键盘匹配
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        letterDict = dict(zip(('1','2','3','4','5','6','7','8','9','0'),('','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz',' ')))
        l = ','.join(letterDict[digits[0]]).split(',') #初始数字形成的字符串列表
        print(l)
        i = 1
        temp = [] #临时列表
        while i < len(digits):
            for letter in l:
                for j in range(len(letterDict[digits[i]])):
                    temp.append(letter + letterDict[digits[i]][j])
                    print(temp)
            l = temp
            temp = []
            i += 1
        return l
s = Solution()
print(s.letterCombinations("22"))

