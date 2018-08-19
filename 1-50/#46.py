#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
import itertools
#Solution 1: Recursive, take any number as first
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = [[num]+p for i,num in enumerate(nums) for p in self.permute(nums[:i]+nums[i+1:])]
        return l
#Solution 2: Recursive, insert first number anywhere

    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]

    #Solution 4: Using the library
    def permute(self, nums):
        return list(itertools.permutations(nums))