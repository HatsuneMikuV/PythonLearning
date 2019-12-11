# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        32
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/11
-------------------------------------------------
   Change Activity:  2019/12/11:
-------------------------------------------------
"""

'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

'''
程序分析：
我们想办法把最小的数放到x上，先将x与y进行比较，
如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。
'''

'''
这里使用的是python  自身的数组排序，只需要将三个数字加到数组里面，然后调用sort函数即可
'''
def indexNumber(numbers):
    numbers.sort()
    return numbers

if __name__ == '__main__':

    input = raw_input('输入三个整数x,y,z：')
    numbers = input.split(',')
    res = indexNumber(numbers)
    print res
    pass