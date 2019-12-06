# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        29
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/6
-------------------------------------------------
   Change Activity:  2019/12/6:
-------------------------------------------------
"""

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''

BW = 1000000
SW = 600000
FW = 400000
TW = 200000
OW = 100000

def one_way(input):
    i = input
    result = 0
    if i > BW:
        result += (i - BW) * 0.01
        i = BW

    if i > SW:
        result += (i - SW) * 0.015
        i = SW

    if i > FW:
        result += (i - FW) * 0.03
        i = FW

    if i > TW:
        result += (i - TW) * 0.05
        i = TW

    if i > OW:
        result += (i - OW) * 0.075
        i = OW

    if i <= OW:
        result += i * 0.1

    return result

ARRAY = [1000000, 600000, 400000, 200000, 100000, 0]
RAT = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
def two_way(input):
    result = 0
    for index in range(0, len(ARRAY)):
        res = ARRAY[index]
        if input > res:
            result += (input - res) * RAT[index]
            input = res

    return result

if __name__ == '__main__':

    input = int(raw_input('净利润:'))

    result = one_way(input)
    result1 = two_way(input)
    print result, result1
    pass