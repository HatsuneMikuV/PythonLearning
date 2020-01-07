# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        51
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/7
-------------------------------------------------
   Change Activity:  2020/1/7:
-------------------------------------------------
"""

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

'''
程序分析：请抓住分子与分母的变化规律。
'''

def countSequence(maxNum):
    a = 1.0
    b = 2.0
    res = 0.0
    for n in range(maxNum):
        res += (b / a)
        a, b = b, a + b
    return res

if __name__ == '__main__':


    print countSequence(20)

    pass