# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        35
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/15
-------------------------------------------------
   Change Activity:  2019/12/15:
-------------------------------------------------
"""

'''
题目：输出 9*9 乘法口诀表。
'''

def printMultList():
    res = ''
    for index in range(1, 10):
        for jndex in range(1, index+1):
            res += '%d X %d = %d ' % (index, jndex, index * jndex)
            jndex += 1
        res += '\n'
    return res


if __name__ == '__main__':
    print printMultList()
    pass