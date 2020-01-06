# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        50
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/6
-------------------------------------------------
   Change Activity:  2020/1/6:
-------------------------------------------------
"""

'''
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''

'''
程序分析：
先把图形分成两部分来看待，
前四行一个规律，后三行一个规律，利用双重for循环，
第一层控制行，第二层控制列。
'''

def printDiamond(count):
    ls1 = ""
    ls2 = ""
    for num in range(1, count + 1, 2):
        width = (count - num) / 2
        ls1 += (" " * width + "*" * num + " " * width + "\n")
        if count != num:
            ls2 = ("\n" + " " * width + "*" * num + " " * width) + ls2
    return ls1 + ls2[1:]

if __name__ == '__main__':

    print printDiamond(7)

    print printDiamond(17)

    pass