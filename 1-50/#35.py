#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return l
        s, f = 0, l-1
        mid = l//2
        while s<f:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                f = mid
                mid = (s+f)//2
            else:
                s = mid + 1
                mid = (s+f)//2
        return s