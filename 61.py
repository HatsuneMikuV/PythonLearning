# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        61
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/10
-------------------------------------------------
   Change Activity:  2020/1/10:
-------------------------------------------------
"""

'''
题目：练习函数调用。
'''

def hello_world():
    print 'hello world'

def three_hellos():
    for i in range(3):
        hello_world()

if __name__ == '__main__':

    three_hellos()

    pass