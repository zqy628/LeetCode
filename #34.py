#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        start = 0
        mid = l // 2
        fin = l - 1
        if l == 0:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]

        if target == nums[start]:
            while start<fin and nums[start + 1] == target:
                start += 1
            return [0,start]
        if target == nums[fin]:
            while start<fin and nums[fin - 1] == target:
                fin -= 1
            return [fin,l-1]
        while start<=mid<=fin:
            print('s%d,f%d,m%d'%(start,fin,mid))
            if target == nums[mid]:
                i = j = mid
                while nums[i-1] == target:
                    i = i-1
                while nums[j+1] == target:
                    j = j+1
                return [i, j]
            elif target <nums[mid]:
                if abs(start-fin) == 1:
                    return [-1, -1]
                fin = mid
                mid = (start+mid) // 2
            else:
                if abs(start-fin) == 1:
                    return [-1, -1]
                start = mid
                mid = (fin+mid) // 2
        return [-1, -1]