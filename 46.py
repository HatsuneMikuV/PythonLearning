# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        46
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/28
-------------------------------------------------
   Change Activity:  2019/12/28:
-------------------------------------------------
"""

'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
'''
1, 找到所有的因数n % i == 0
2, 计算所有i的和 n相比较
3, 保存相等的完数和它的因数
'''

def complete_number(result):
    res = {}
    for n in range(1, result + 1):
        result = 0
        ls = []
        for index in range(1, n):
            if n % index == 0:
                result += index
                ls.append(index)
        if n == result:
            res[n] = ls
    return res

if __name__ == '__main__':

    print complete_number(1000)

    pass