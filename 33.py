# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        33
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/12
-------------------------------------------------
   Change Activity:  2019/12/12:
-------------------------------------------------
"""

'''
题目：斐波那契数列。
'''

'''
程序分析：斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、...
'''

def fibonacci(index):
    result = 0
    resList = []
    resCount = 0
    a, b = 0, 1
    resList.append(0)
    for i in range(index - 1):
        a, b = b, a + b
        result += a
        resList.append(a)
        resCount = b

    return resCount, result, resList

if __name__ == '__main__':
    resCount, result, resList = fibonacci(10)
    print resCount, result, resList
    pass