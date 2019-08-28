# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_5
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-28
-------------------------------------------------
   Change Activity:  2019-08-28:
-------------------------------------------------
"""


class Solution(object):

    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0




    def orignal(self,nums1,  nums2):
        ll = nums1 + nums2
        ll.sort()
        print ll
        count = len(ll)
        num1 = ll[count / 2]
        num2 = 0
        if count % 2 == 0:
            num2 = ll[count / 2 - 1]

        if num2 > 0:
            return (num2 + num1) * 0.5

        return num1




if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 6]
    b = [3, 4, 6, 7, 8]

    so = Solution()
    l = so.findMedianSortedArrays(a, b)
    print l

    l = so.orignal(a, b)
    print l

    pass