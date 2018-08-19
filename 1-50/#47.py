#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        if nums == []:
            l.append([])
        for i, num in enumerate(nums):
            for p in self.permuteUnique(nums[:i] + nums[i + 1:]):
                if [num] + p not in l:
                    l.append([num] + p)
        return l