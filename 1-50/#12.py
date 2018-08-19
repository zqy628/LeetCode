#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
crossin教室有类似题
罗马数字采用七个罗马字母作数字、即 I（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。
它有一套不同于阿拉伯数字的写法规则，简单来说可以总结为：
1.相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；
2.小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
3.小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9；
4.在一个数的上面画一条横线，表示这个数增值 1,000 倍。
'''


class Solution:
    # 阿拉伯数字转罗马数字
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        i = 0
        while num:
            roman += num // values[i] * numerals[i]
            num = num % values[i]
            i += 1
        return roman

    # 简单方法
    def itr(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]

    # 罗马数字转阿拉伯数字
    def romanToInt(s):

        d = dict(zip('IXCMVLD', (1, 10, 100, 1000, 5, 50, 500)))
        res, p = 0, 'I'
        # 逆序逐一遍历
        # 使用逆序的好处在于，每次只需对一位罗马数字进行加或减的操作
        # 使用顺序的话，可能为两位
        for c in s[::-1]:
            if d[c] < d[p]:
                res = res - d[c]
            else:
                res = res + d[c]
            p = c

        return res
