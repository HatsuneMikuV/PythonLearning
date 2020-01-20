# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        71
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/20
-------------------------------------------------
   Change Activity:  2020/1/20:
-------------------------------------------------
"""

'''
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
'''
X = [[12,7,3],
     [4 ,5,6],
     [7 ,8,9]]

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

if __name__ == '__main__':

    l = []
    for i in range(len(X)):
        ll = []
        for j in range(len(X[i])):
            ll.append(X[i][j] + Y[i][j])
        l.append(ll)
    print l
    pass