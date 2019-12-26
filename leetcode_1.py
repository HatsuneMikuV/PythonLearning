# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_1
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-23
-------------------------------------------------
   Change Activity:  2019-08-23:
-------------------------------------------------
"""

'''
自除数
'''

'''
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
'''

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    list = []
    for i in range(left, right):
        tmp = i
        while tmp:
            mod = tmp % 10
            if mod == 0:
                break
            else:
                if i % mod == 0:
                    tmp /= 10
                else:
                    break
        if tmp == 0:
            list.append(i)
            continue


if __name__ == '__main__':

    list = selfDividingNumbers(1, 22)
    print list
