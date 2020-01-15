# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        66
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/15
-------------------------------------------------
   Change Activity:  2020/1/15:
-------------------------------------------------
"""
'''
题目：
有一个已经排好序的数组。
现输入一个数，要求按原来的规律将它插入数组中。
'''

def insert_num(ll, num):
    if type(ll) != list:
        return ll
    if len(ll) == 0 or num >= ll[-1]:
        ll.append(num)
        return ll
    if num <= ll[0]:
        ll.insert(0, num)
        return ll

    cur = -1
    for i in range(len(ll)):
        if num > ll[i]:
            cur = i
    ll.insert(cur + 1, num)
    return ll


if __name__ == '__main__':

    print insert_num([0, 1], 3)
    print insert_num([4, 5], 3)
    print insert_num([0, 1, 4, 5], 3)

    pass