# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        48
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/3
-------------------------------------------------
   Change Activity:  2020/1/3:
-------------------------------------------------
"""

'''
题目：
猴子吃桃问题：
猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。
求第一天共摘了多少。
'''

'''
程序分析：采取逆向思维的方法，从后往前推断。
'''

def remainCount(days):
    if days <= 0:
        return 0

    current = 1
    for index in range(days - 1):
        current = (current + 1) * 2
    return current

if __name__ == '__main__':

    print remainCount(10)
    pass