# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        73
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/21
-------------------------------------------------
   Change Activity:  2020/1/21:
-------------------------------------------------
"""

'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''

def sq_sum(num):
    return num * num

if __name__ == '__main__':

    cycle = True
    while cycle:
        num = int(raw_input('请输入一个数字：'))
        res = sq_sum(num)
        print '平方结果', res
        if res < 50:
            cycle = False

    pass