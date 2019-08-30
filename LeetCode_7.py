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