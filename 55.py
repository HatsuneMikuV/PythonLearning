# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        55
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/8
-------------------------------------------------
   Change Activity:  2020/1/8:
-------------------------------------------------
"""


'''
题目：
有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。
请问第五个人多大？
'''

def recursive_age(age, num):

    if num <= 1:
        return age
    return recursive_age(age + 2, num - 1)


if __name__ == '__main__':

    print recursive_age(10, 5)

    print recursive_age(10, 1)

    print recursive_age(10, 0)


    pass