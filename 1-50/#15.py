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
    #超出时间复杂度
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        r = [] #存放重复元素
        nums_set = list(set(nums)) #去重
        #找出重复元素
        for num in nums_set:
            if nums.count(num) >= 2:
                r.append(num)
        #创建一个迭代器，返回iterable中所有长度为r的子序列,不带重复
        for i in itertools.combinations(nums_set,3):
            if sum(i) == 0:
                l.append(list(i))
        if r:
            for j in r:
                if j != 0 and -2*j in nums:
                    l.append([j,j,-2*j])
                elif j == 0 and nums.count(0) >= 3:
                    l.append([0,0,0])
        return l

    def threeSum1(self, nums):
        res = []
        nums.sort()
        if nums[:3].count(0) >= 3:
            res.append(nums)
        for i in range(len(nums)-2):
            if nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: #忽略重复
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res
s = Solution()
print(s.threeSum1([0,0,0]))