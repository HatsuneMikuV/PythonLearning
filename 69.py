# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        69
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/19
-------------------------------------------------
   Change Activity:  2020/1/19:
-------------------------------------------------
"""


'''
题目：学习使用auto定义变量的用法。
'''

num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1


if __name__ == '__main__':

    for i in range(3):
        print 'The num = %d' % num
        num += 1
        autofunc()
    pass