#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        flag = len(num) % 2
        mid = len(num) // 2
        if flag == 0:
            return (num[mid-1] + num[mid]) / 2
        else:
            return num[mid]
s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))