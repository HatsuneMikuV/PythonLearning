# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        70
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/19
-------------------------------------------------
   Change Activity:  2020/1/19:
-------------------------------------------------
"""

'''
题目：模仿静态变量(static)另一案例。
类似面对对象编程的属性
'''

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()