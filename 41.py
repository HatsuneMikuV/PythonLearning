# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        41
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/18
-------------------------------------------------
   Change Activity:  2019/12/18:
-------------------------------------------------
"""

'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

'''
1，k从第一个素数开始2
2，用n除k 整除 则k是一个质因数
3，不能整除则k增加1，循环2操作
4，直到k等于n时，即为最后一个质因数，结束循环
'''

def mult_number(result):
    n = result
    k = 2
    res = []
    while k <= n:
        if n % k == 0:
            n = n / k
            res.append(k)
        else:
            k = k + 1

    return res

if __name__ == '__main__':

    number = 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
    res = map(str, mult_number(number))
    print '%d = ' % (number), ' * '.join(res)

    pass