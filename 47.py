# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        47
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/3
-------------------------------------------------
   Change Activity:  2020/1/3:
-------------------------------------------------
"""


'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

'''
程序分析：1.第一次是100高度,回弹50
        2.第二次是50高度,回弹25，
        3.因此除第一次外，都会有两次回弹高度  height * 2，累加后减去第一次多加100即为总的高度
        
'''

def falldown(times, height):
    if times <= 0 or height <= 0:
        return 0, 0

    totalHeight = -height
    lastHeight= height
    for index in range(times):
        totalHeight += lastHeight * 2.0
        lastHeight = lastHeight / 2.0
        print totalHeight, lastHeight

    return totalHeight, lastHeight


if __name__ == '__main__':
    print falldown(10, 100)
    pass