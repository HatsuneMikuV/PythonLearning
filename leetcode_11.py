# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_11
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/6
-------------------------------------------------
   Change Activity:  2019/12/6:
-------------------------------------------------
"""

'''
Regular Expression Matching
'''


def isMatch_One(str, pattern):

    if len(str) != len(pattern):
        return False

    for i in range(len(pattern)):
        if pattern[i] != str[i]:
            return False

    return True

def isMatch_Two(str, pattern):

    i, j = 0, 0
    while j < len(pattern):
        if i >= len(str):
            return False
        j += 1
        i += 1
        if pattern[j] != str[i]:
            return False
    return j == len(str)

def isMatch_Thr(str, pattern):

    if len(pattern) is 0:
        return len(str) is 0
    res = len(str) != 0 and pattern[0] == str[0]
    return res and isMatch_Thr(str[1:], pattern[1:])

def isMatch_Fou(str, pattern):

    if not pattern:
        return not str

    res = bool(str) and pattern[0] in {str[0], '.'}
    return res and isMatch_Thr(str[1:], pattern[1:])

def isMatch_Fiv(str, pattern):

    if not pattern:
        return not str

    res = bool(str) and pattern[0] in {str[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return isMatch_Fiv(str, pattern[2:]) or res and isMatch_Fiv(str[1:], pattern)
    else:
        return res and isMatch_Fiv(str[1:], pattern[1:])



if __name__ == '__main__':

    str = 'mississippi'
    pattern = 'mis*is*.p*.'

    # str = 'aab'
    # pattern = 'c*a*b'

    res1 = isMatch_One(str, pattern)
    print res1

    res2 = isMatch_Two(str, pattern)
    print res2

    res3 = isMatch_Thr(str, pattern)
    print res3

    res4 = isMatch_Fou(str, pattern)
    print res4

    res5 = isMatch_Fiv(str, pattern)
    print res5

    pass