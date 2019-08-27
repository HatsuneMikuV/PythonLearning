# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_4
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-27
-------------------------------------------------
   Change Activity:  2019-08-27:
-------------------------------------------------
"""
'''
Longest Substring Without Repeating Characters
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans

if __name__ == '__main__':

    lenth = Solution().lengthOfLongestSubstring("abcabcsecaacbcbcbcbccb")
    print lenth
    pass
