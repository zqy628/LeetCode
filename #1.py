#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # #时间复杂度不满足要求
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        #[3,3] 6 测试不通过  调整为逆序寻找通过
        for i in range(len(nums))[::-1]:
            print(i)
            other = target - nums[i]
            if other in nums:
                j = nums.index(other)
                if i != j:
                    return [i,j]
        return None
s = Solution()
print(s.twoSum([3,2,4],6))

#大神解答：
class Solution1(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print(buff_dict)
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
s = Solution1()
print(s.twoSum([11, 2, 2, 7, 11, 15],9))
