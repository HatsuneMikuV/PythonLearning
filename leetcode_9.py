# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_9
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-09-05
-------------------------------------------------
   Change Activity:  2019-09-05:
-------------------------------------------------
"""


def intNumber(str):
    if len(str) <= 0:
        return 0
    l = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    st = str
    while st[0] == ' ':
        st = st[1:]
        if len(st) <= 0:
            return 0
    if len(st) <= 0:
        return 0
    right = True
    if st[0] == '-' or st[0] == '+':
        right = st[0] == '+'
        st = st[1:]
    if len(st) <= 0:
        return 0
    if st[0] not in l:
        return 0
    num = []
    for s in st:
        if s == '.' or s not in l:
            break
        num.append(l[s])
    count = len(num)
    index = 0
    number = 0
    while index < count:
        s = num[index]
        number += s * 10 ** (count - index - 1)
        index += 1

    if not right:
        number = 0 - number

    if number > 2 ** 31 - 1 or number < -2 ** 31:
        if right:
            return 2 ** 31 - 1
        return -2 ** 31
    return number


if __name__ == '__main__':


    print intNumber('42')
    print intNumber('   -42')
    print intNumber('4193 with words')
    print intNumber('words and 987')
    print intNumber('-91283472332')
    print intNumber('')
    print intNumber(' ')
    print intNumber('-')
    print intNumber("3.14159")
    print intNumber('+1')
    print intNumber('+-2')
    print intNumber('-2')
    print intNumber('  -0012a42')
    print intNumber("   +0 123")
    print intNumber('mm-n66')

    pass