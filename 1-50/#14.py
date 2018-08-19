#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        lenth = len(strs)
        if not strs:
            return ''
        else:
            i = 1
            while i <= len(strs[0]):
                try:
                    prefix_ = strs[0][:i]
                except:
                    return prefix
                else:
                    for j in range(1,lenth):
                        if prefix_ == strs[j][:i]:
                            continue
                        else:
                            return prefix
                prefix = prefix_
                i += 1
            return prefix
s = Solution()
print(s.longestCommonPrefix(['']))