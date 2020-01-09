# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        56
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/9
-------------------------------------------------
   Change Activity:  2020/1/9:
-------------------------------------------------
"""

'''
题目：
给一个不多于5位的正整数，
要求：
一、求它是几位数，
二、逆序打印出各位数字。
'''

def reverseNum(num):
    numStr = str(num)
    if '-' in numStr:
        numStr = numStr.replace('-', '')
    return len(numStr), numStr[::-1]


if __name__ == '__main__':

    print reverseNum(12345)
    print reverseNum(+12345)
    print reverseNum(-12345)

    pass