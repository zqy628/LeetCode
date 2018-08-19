#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

#Two strings are anagrams if and only if their sorted strings are equal.
class Solution(object):
    def groupAnagrams(self, strs):
        ans = dict()
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l = len(strs)
        # strs_ = strs
        list_ = []
        strs_ = []
        for i,str in enumerate(strs):
            # strs_[i] = sorted(list(str))
            if sorted(list(str)) not in list_:
                list_.append(sorted(list(str)))
                strs_.append([strs[i]])
            else:
                for j,list1 in enumerate(list_):
                    if list1 == sorted(list(str)):
                        strs_[j].append(strs[i])
        return strs_
        # print(strs_)
        #
        # for i, str in enumerate(strs_):

s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])