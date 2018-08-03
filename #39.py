#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates,target,0,[],res)
        return res

    def dfs(self, nums,target,index,path,res):
        if target<0:
            return
        if target == 0:
            res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums,target-nums[i],i,path+[nums[i]],res)


#
class Solution1:
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		res = []
		def com(nums, target, i, cur):
			if i == len(nums):
				return
			if target == 0:
				res.append(list(cur))
				return
			if nums[i] <= target:
				cur.append(nums[i])
				com(nums, target - nums[i], i, cur)
				cur.pop()
				com(nums, target, i + 1, cur)
			else:
				com(nums, target, i + 1, cur)
		com(candidates, target, 0, [])
		return res