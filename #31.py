#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

#1.从后往前找到第一个不是升序的元素
#2.在此元素后面的元素中寻找一个刚好大于它的元素，并调换位置
#3.将此元素位置后方的元素全都逆序
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #没有比他更小的排列了，输出第一个
        if nums == sorted(nums)[::-1]:
            # print('True')
            nums.sort()
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[i-1]:
                    pos = i - 1
                    break
            # print('pos:',pos)
            sub = -nums[pos] + nums[pos+1]
            rpos = 0
            for j in range(pos+1,len(nums)):
                csub = -nums[pos] + nums[j]
                if csub <= sub and csub > 0:
                    sub = csub
                    rpos = j
            nums[pos],nums[rpos] = nums[rpos],nums[pos]
            nums[pos+1:] = nums[pos+1:][::-1]