# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        59
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/10
-------------------------------------------------
   Change Activity:  2020/1/10:
-------------------------------------------------
"""

'''
题目：按相反的顺序输出列表的值。
'''

def reverseList(ll):
    for objc in ll[::-1]:
        print objc

if __name__ == '__main__':

    reverseList(["one", "two", "three"])

    pass