#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
给定n个非负整数a1，a2，...，an，其中每个代表坐标（i，ai）处的一个点。连接（i，ai）和（i，0）处画出n条垂直线。
找到两个端点，垂直两条线，它们与x轴一起形成一个容器，使得包含最多的水。
Note: You may not slant the container and n is at least 2.
'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
