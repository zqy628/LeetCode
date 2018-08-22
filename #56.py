#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # l = len(intervals)
        # print (intervals[0].start)
        intervals.sort(key = lambda interval:interval.start)
        flag = True
        while flag:
            l = len(intervals)
            flag = False
            for i in range(l-1,0,-1):
                if intervals[i-1].end >= intervals[i].start:
                    if intervals[i-1].end >= intervals[i].end:
                        # intervals[i-1].end = intervals[i].end
                        intervals.pop(i)
                    else:
                        intervals[i-1].end = intervals[i].end
                        intervals.pop(i)
                    flag = True
                    break
        return intervals

