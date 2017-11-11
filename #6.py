#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #先设置一个矩阵数组
        lenth = len(s)
        if numRows == 1 or lenth <= 1:
            return s
        else:
            quo = lenth // (numRows - 1) #商
            re = lenth % (numRows - 1) #余数
            if quo % 2 == 0:
                numCols = 1 + quo // 2 * (numRows-1)
            else:
                numCols = 1 + (quo-1) // 2 * (numRows-1) + (re+numRows-2) % (numRows-1)
            matrix = [[' ' for i in range(numCols)] for j in range(numRows)]
            i = 0
            j = 0
            matrix[i][j] = s[0] #先填充首字母
            for index in range(1,lenth):
                if ((index-1) // (numRows-1)) % 2 == 0:
                    i += 1
                    matrix[i][j] = s[index]
                else:
                    i -= 1
                    j += 1
                    matrix[i][j] = s[index]
            for i in range(numRows):
                print(matrix[i]),
            zigzag = ''
            for i in range(numRows):
                zigzag += ''.join(matrix[i])
            return zigzag.replace(' ','')

    #简便解法
    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)
s = Solution()
print(s.convert("BFSDGSDFGSDGNSGJIOIHJSIFGHURTHSUGNIMSMSFEREJETIRETGRSNGUSFGGNIMAMADEWENMAMDWENNISHUONEMINGZHINIBUZAIHAISHIHUIWEN", 20))