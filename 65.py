# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        65
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/15
-------------------------------------------------
   Change Activity:  2020/1/15:
-------------------------------------------------
"""


'''
题目：求一个3*3矩阵主对角线元素之和。
'''

def sum_diagonal(ll):
    if type(ll) != list:
        return 0
    if len(ll) == 0:
        return 0
    res = 0
    for i in range(len(ll)):
        res += ll[i][i]
    return res


if __name__ == '__main__':


    print sum_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    pass