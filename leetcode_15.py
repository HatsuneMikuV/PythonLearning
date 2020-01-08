# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_15
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/8
-------------------------------------------------
   Change Activity:  2020/1/8:
-------------------------------------------------
"""

'''
Longest Common Prefix

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z
'''

def findlongprefix(ls):
    if type(ls) != list:
        return ''
    if len(ls) == 0:
        return ''
    prefix = ls[0]
    print prefix
    for i in range(len(ls)):
        while ls[i].find(prefix) != 0:
            print ls[i]
            prefix = prefix[0:len(prefix) - 1]
            if len(prefix) == 0:
                return ''
    return prefix


if __name__ == '__main__':

    print findlongprefix(["flower", "flow", "flight"])

    pass