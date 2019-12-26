# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        44
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/26
-------------------------------------------------
   Change Activity:  2019/12/26:
-------------------------------------------------
"""

'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''


if __name__ == '__main__':

    input = raw_input('请输入一个字符串:\n')

    index = 0
    word = 0
    num = 0
    space = 0
    other = 0
    while index < len(input):
        ss = input[index]
        index += 1
        if ss.isalpha():
            word += 1
        elif ss.isspace():
            space += 1
        elif ss.isdigit():
            num += 1
        else:
            other += 1

    print "words: %d, numbers: %d, spaces: %d, others: %d" % (word, num, space, other)

    pass