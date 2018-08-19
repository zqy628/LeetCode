#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

atoi (表示 ascii to integer)是把字符串转换成整型数的一个函数，应用在计算机程序和办公软件中。atoi( ) 函数会扫描参数 nptr字符串，跳过前面的空白字符（例如空格，tab缩进）等。
'''
#失败了
import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_none = re.findall('[+-]{1}\D+\d+',str)
        if str_none:
            print('000')
            return 0
        str_none1 = re.findall('[+-]{2,}\d+',str)
        if str_none1:
            print('111')
            return 0
        str_none2 = re.findall('[^\d]+\d+',str)
        if str_none2:
            print('222')
            return 0
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
#大神简洁版代码
class Solution1(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        # if len(ls) == 0 : return 0
        if len(s) == 0: return 0
        ls = list(s.strip())

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            #ord""" Return the Unicode code point for a one-character string. """
            ret = ret * 10 + ord(ls[i]) - ord('0') #这一步精髓
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))
s = Solution()
print(s.myAtoi('-1'))