# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        LeetCode_7
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-30
-------------------------------------------------
   Change Activity:  2019-08-30:
-------------------------------------------------
"""

'''
ZigZag Conversion    
'''

'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if len(s) <= 0 or len(s) <= numRows or numRows == 1:
        return s
    list = {}
    row = 0
    add = True
    for i in range(len(s)):
        s1 = ''
        if row in list:
            s1 = list[row]
        list[row] = s1 + s[i]
        if add:
            row += 1
        else:
            row -= 1
        if row == numRows - 1:
            add = False
        elif row == 0:
            add = True
    return ''.join(list.values())

if __name__ == '__main__':

    print convert("LEETCODEISHIRING", 3)
    print convert("LEETCODEISHIRING", 4)
    print convert("a", 2)
    print convert("", 1)
    print convert("aa", 1)
    pass