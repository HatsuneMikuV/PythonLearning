# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        62
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/10
-------------------------------------------------
   Change Activity:  2020/1/10:
-------------------------------------------------
"""

'''
题目：文本颜色设置。
'''

class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':

    print bColors.WARNING + "警告的颜色字体?" + bColors.ENDC

    pass