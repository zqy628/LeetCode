#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #调用方法
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        l = len(nums)
        if l == 0:
            return -1
        if target>=nums[0]:
            for i in range(l):
                if target == nums[i]:
                    return i
                elif target < nums[i]:
                    return -1
                elif i == l-1:
                    return -1
        elif target <= nums[-1]:
            for j in range(l)[::-1]:
                if target == nums[j]:
                    return j
                elif target > nums[j]:
                    return -1
                elif j == 0:
                    return -1
        else:
            return -1
