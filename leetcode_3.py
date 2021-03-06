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

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
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


