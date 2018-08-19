#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.(不能使用乘除和求余数运算)

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''
# Time Limit Exceeded (-2147483648,-1)
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            positive = -1
        else:
            positive = 1
        dividend, divisor = abs(dividend), abs(divisor)
        plus = 0
        i = 0
        while dividend - plus >= divisor:
            plus += divisor
            i += 1
        return i * positive

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            positive = -1
        else:
            positive = 1
        dividend, divisor = abs(dividend), abs(divisor)
        i = 0
        while dividend >= divisor:
            temp, res = divisor, 1
            while dividend >= temp:
                i += res
                dividend -= temp
                res <<= 1
                temp <<= 1

        return min(max(i * positive,-2147483648), 2147483647)
