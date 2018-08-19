#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        rsum = sum(nums[:3])
        diff = abs(rsum - target)
        for i in range(len(nums)-2):
            if nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff_ = s - target
                if diff_ == 0:
                    return target
                elif diff_ > 0:
                    if diff_ < diff:
                        rsum = s
                        diff = abs(diff_)
                    r -= 1
                else:
                    if abs(diff_) < diff:
                        rsum = s
                        diff = abs(diff_)
                    l += 1
                print(rsum)
        return rsum
s = Solution()
print(s.threeSumClosest([0,2,1,-3],1))
        

