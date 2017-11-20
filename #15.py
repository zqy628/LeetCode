#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import itertools
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        r = [] #存放重复元素
        #找出重复元素
        for i,k in itertools.groupby(nums,len):
            if i >= 2:
                r += k
        nums = list(set(nums)) #去重
        #创建一个迭代器，返回iterable中所有长度为r的子序列,不带重复
        for i in itertools.combinations(nums,3):
            if sum(i) == 0:
                l.append(list(i))
        if r:
            for j in r:
                
        return l