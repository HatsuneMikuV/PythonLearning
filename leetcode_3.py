# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_3
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-08-26
-------------------------------------------------
   Change Activity:  2019-08-26:
-------------------------------------------------
"""

'''
Add Two Numbers
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        list1 = []

        ll1 = l1
        ll2 = l2
        l3 = ListNode(0)
        l = ListNode(0)
        l3.next = l
        ten = 0
        while ll1 or ll2:
            num1 = ll1.val if ll1 else 0
            num2 = ll2.val if ll2 else 0
            num = num1 + num2 + ten

            if num > 9:
                num = num % 10
                ten = 1
            else:
                ten = 0


            l.next = ListNode(num)
            l = l.next

            if ll1:
                ll1 = ll1.next
            if ll2:
                ll2 = ll2.next

            if ten == 1:
                l.next = ListNode(1)

        return l3.next.next



if __name__ == '__main__':


    l1 = ListNode(9)

    l2 = ListNode(9)

    result = Solution().addTwoNumbers(l1, l2)

    print result
    while result:
        print result.val, '->'
        result = result.next

    pass


