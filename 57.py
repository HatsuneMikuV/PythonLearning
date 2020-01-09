# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        57
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/9
-------------------------------------------------
   Change Activity:  2020/1/9:
-------------------------------------------------
"""


'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''


def isReverseNum(num):
    if num < 0:
        return False
    numStr = str(num)
    if numStr == numStr[::-1]:
        return True
    return False


if __name__ == '__main__':

    print isReverseNum(0)
    print isReverseNum(-1)
    print isReverseNum(1)
    print isReverseNum(123)
    print isReverseNum(121)
    print isReverseNum(-121)


    pass