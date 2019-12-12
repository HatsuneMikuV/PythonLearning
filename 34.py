# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        34
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/12
-------------------------------------------------
   Change Activity:  2019/12/12:
-------------------------------------------------
"""

'''
题目：将一个列表的数据复制到另一个列表中。
'''

'''
程序分析：使用列表[:]。
'''

def copyList(array):
    return array[:]

if __name__ == '__main__':

    res = copyList([1, 2, 3])
    print res

    pass