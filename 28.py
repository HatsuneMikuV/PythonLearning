# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        28
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/10/9
-------------------------------------------------
   Change Activity:  2019/10/9:
-------------------------------------------------
"""

'''
Python 练习实例1
Python 100例 Python 100例

题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

程序源代码：
'''


if __name__ == '__main__':

    l = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    l.append((i, j, k))
    print len(l)
    print l
    pass