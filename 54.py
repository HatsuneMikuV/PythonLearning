# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        54
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/8
-------------------------------------------------
   Change Activity:  2020/1/8:
-------------------------------------------------
"""

'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

def recursive(ss):
    if type(ss) != str:
        return ''
    if len(ss) == 0:
        return ''
    return recursive(ss[1:]) + ss[:1]

if __name__ == '__main__':


    print recursive("123")

    print recursive("1")

    print recursive(1)

    pass