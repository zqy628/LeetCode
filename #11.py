#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
梯形桶装水问题
'''
#超出时间复杂度
# class Solution:
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         lenth = len(height)
#         water = 0
#         for i in range(lenth):
#             for j in range(lenth-1,i,-1):
#                 if height[j] > height[i]:
#                     water = max((j-i)*height[i],water)
#                 else:
#                     water = max((j-i)*height[j],water)
#         return water

#这种方法背后的直觉是，线条之间形成的区域总是受到较短线条高度的限制。 而且，线越远，获得的面积就越大。
#我们采取两个指针，一个在开始，一个在数组的结尾，构成行的长度。
# 而且，我们保持一个可变的maxareamaxarea来存储迄今为止获得的最大面积。
# 在每个步骤中，我们找出它们之间形成的区域，更新maxareamaxarea，并将指针指向朝向较短的一端缩短一步。
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenth = len(height)
        water = 0
        for i in range(lenth):
            

        return water


s = Solution()
print(s.maxArea())