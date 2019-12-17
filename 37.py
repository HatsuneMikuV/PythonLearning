# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        37
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/17
-------------------------------------------------
   Change Activity:  2019/12/17:
-------------------------------------------------
"""

'''
题目：暂停一秒输出，并格式化当前时间。
'''
import time
if __name__ == '__main__':

    print '开始', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    time.sleep(1)
    print '结束', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    pass