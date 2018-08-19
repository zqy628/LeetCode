#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''
import time

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:return 0
        if max(nums) == 1:
            return l-1
        # index = 0
        count = 1
        li = [nums[i] >= l-1-i for i in range(l-1)]
        print(li)
        while li[0] != True:
            for i in range(len(li)):
                if li[i]:
                    for j in range(l-1):
                        if nums[j] >= abs(i-j):
                            li[j] = True
            #这样更快
            # i = li.index(True)
            # for j in range(l - 1):
            #     if nums[j] >= abs(i - j):
            #         li[j] = True
            #         break
            count += 1
            if li[0]:
                return count
        return count
#####
class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

s = Solution()
t = time.time()
print(s.jump([]))
print(time.time()-t)