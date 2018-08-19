#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 1:return True
        elif nums[0] == 0:
            return False
        if max(nums) == min(nums) == 1:
            return True
        index = 0
        li = [nums[i] >= l-1-i for i in range(l-1)]
        # print(li)
        if li[0]:
                return True
        while li[0] != True:
            if True in li:
                i = li.index(True)
            else:
                return False
            flag = False
            for j in range(i):
                if nums[j] >= abs(i - j):
                    li[j] = True
                    flag = True
                    # break
            if not flag:
                return False
            if li[0]:
                return True
            # print(li)
        return False
