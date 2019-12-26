# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_10
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-09-09
-------------------------------------------------
   Change Activity:  2019-09-09:
-------------------------------------------------
"""

'''
Palindrome Number
'''

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        ss = str(x)
        if len(ss) <= 0:
            return False

        s = ss[::-1]
        if s == ss:
            return True
        return False


    def isPalindromeTwo(self, x):

        ss = str(x)
        if len(ss) <= 0:
            return False

        left = 0
        right = len(ss) - 1

        while left <= right:
            l = ss[left]
            r = ss[right]
            print l, r
            if l != r:
                return False
            else:
                left += 1
                right -= 1

        return True


if __name__ == '__main__':

    ss = Solution()
    print ss.isPalindrome(123321)
    print ss.isPalindromeTwo(123321)

    pass