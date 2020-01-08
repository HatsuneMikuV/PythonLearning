# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        53
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/8
-------------------------------------------------
   Change Activity:  2020/1/8:
-------------------------------------------------
"""

'''
题目：利用递归方法求5!。
'''

def recursive(num):
    if num <= 1:
        return 1
    return num * recursive(num - 1)

if __name__ == '__main__':

    print recursive(5)

    print recursive(1)

    print recursive(0)

    pass