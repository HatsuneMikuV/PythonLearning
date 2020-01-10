# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        58
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/10
-------------------------------------------------
   Change Activity:  2020/1/10:
-------------------------------------------------
"""


'''
题目：
请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
'''
WEEK = {"M": "Monday", "Tu": "Tuesday", "W": "Wednesday", "Th": "Thursday", "F": "Friday", "Sa": "Saturday", "Su": "Sunday"}


def judeDay(week):
    key = week[:1]
    if key in WEEK:
        return WEEK[key]
    return WEEK[week[:2]]



if __name__ == '__main__':

    print judeDay("Tu")
    print judeDay("F")
    print judeDay("Th")
    print judeDay("Sa")
    print judeDay("Sa")
    print judeDay("Su")
    print judeDay("M")

    pass