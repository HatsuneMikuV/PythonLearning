# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        40
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/18
-------------------------------------------------
   Change Activity:  2019/12/18:
-------------------------------------------------
"""

'''
题目：
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''

'''
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
'''

if __name__ == '__main__':

    res = []
    for number in range(100, 1000):
        h = int(number / 100)
        t = int((number - h * 100) / 10)
        g = number - h * 100 - t * 10
        total = h ** 3 + t ** 3 + g ** 3
        if total == number:
            res.append('%d = %d^3 + %d^3 + %d^3' % (number, h, t, g))
    print '\n'.join(res)
    pass