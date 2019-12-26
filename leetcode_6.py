# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_6
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-29
-------------------------------------------------
   Change Activity:  2019-08-29:
-------------------------------------------------
"""

'''
Longest Palindromic Substring
'''

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

import cmath
# class Solution(object):
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    # 预处理
    s = '#' + '#'.join(s) + '#'

    RL = [0] * len(s)
    MaxRight = 0
    pos = 0
    MaxLen = 0
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2 * pos - i], MaxRight - i)
        else:
            RL[i] = 1
        # 尝试扩展，注意处理边界
        while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] += 1
        # 更新MaxRight,pos
        if RL[i] + i - 1 > MaxRight:
            MaxRight = RL[i] + i - 1
            pos = i
        # 更新最长回文串的长度
        MaxLen = max(MaxLen, RL[i])
    return MaxLen - 1


if __name__ == '__main__':

    print longestPalindrome("aaa")
    pass
