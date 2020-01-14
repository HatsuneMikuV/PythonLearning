# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        64
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/14
-------------------------------------------------
   Change Activity:  2020/1/14:
-------------------------------------------------
"""

'''
题目：对10个数进行排序。
'''

def sort_one(ll):
    if type(ll) != list:
        return ll
    if len(ll) == 0:
        return ll
    l = []
    for i in range(len(ll)):
        cur = -1
        for j in range(len(l)):
            if ll[i] > l[j]:
                cur = j
        l.insert(cur + 1, ll[i])
    return l

if __name__ == '__main__':

    ll = [3, 2, 1, 7, 9, 5, 6, 4, 8, 0]
    print sort_one(ll)

    l = [3, 2, 1, 7, 9, 5, 6, 4, 8, 0]
    l.sort()
    print l

    pass