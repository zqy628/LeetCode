#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

atoi (表示 ascii to integer)是把字符串转换成整型数的一个函数，应用在计算机程序和办公软件中。atoi( ) 函数会扫描参数 nptr字符串，跳过前面的空白字符（例如空格，tab缩进）等。
'''
import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_none = re.findall('[+1]')
        if str == '' or str == '+' or str == '-' or '+-' in str or '-+' in str:
            return 0
        else:
            str_ = re.findall('[+-]?\d+',str)
            print(str_)
            if str_ != []:
                str_ = int(str_[0])
                print(str_)
                if str_ > 2147483647:
                    return 2147483647
                elif str_ < -2147483648:
                    return -2147483648
                else:
                    return str_
            else:
                return 0

s = Solution()
print(s.myAtoi('1'))