# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_2
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-25
-------------------------------------------------
   Change Activity:  2019-08-25:
-------------------------------------------------
"""


'''
两数之和
'''


if __name__ == '__main__':

    nums = [3, 2, 4]

    target = 6

    result = {}
    list = []
    for index, num in enumerate(nums):
        other = target - num
        if other in result:
            list = [result[other], index]
        result[num] = index

    print list
