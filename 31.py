# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        31
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/10
-------------------------------------------------
   Change Activity:  2019/12/10:
-------------------------------------------------
"""


'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
# date  20191210
dayList = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
def calculateTodayNumber(date):
    num = 0
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    num += dayList[month - 1]
    num += day
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        num += 1
    return  num

if __name__ == '__main__':

    while 1 :
        input = raw_input('年月日(20191210, -1->exit)：')
        if input == '-1':
            break

        if len(input) == 8:
            res = calculateTodayNumber(input)
            print input, '是今年第', res, '天'
        else:
            print '输入不正确'        

    pass