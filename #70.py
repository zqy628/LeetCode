#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Status: Time Limit Exceeded
        # if n == 2:
        #     return 2
        # if n == 1:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        #Approach 2: Recursion with memorization

        #Fibonacci Number
        a,b = 1,1
        for _ in range(n):
            a,b = b,a+b
        return a


