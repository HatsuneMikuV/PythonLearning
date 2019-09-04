# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     six
   Description :
   Author :       joe
   date：          2019-07-22
-------------------------------------------------
   Change Activity:
                   2019-07-22:
-------------------------------------------------
"""

# Python 条件语句
# Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

# 例1：if 基本用法
flag = False
name = 'luren'
if name == 'python':  # 判断变量是否为 python
    flag = True  # 条件成立时设置标志为真
    print 'welcome boss'  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称



# if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系
# 例2：elif用法
num = 5
if num == 3:  # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print 'roadman'  # 条件均不成立时输出


# 由于 python 并不支持 switch 语句，所以多个条件判断，
# 只能用 elif 来实现，如果判断需要多个条件需同时判断时，
# 可以使用 or （或），表示两个条件有一个成立时判断条件成功；
# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。

# 例3：if语句多个条件
num = 9
if num >= 0 and num <= 10:
    print "在0~10之间"


num = 10
if num < 0 or num > 10:
    print "小于0或大于10"
else:
    print "在0~10之间"

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print "在0~5之间 或者 在10~15之间"

# 当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，
# 此外 and 和 or 的优先级低于 >（大于）、 < （小于）等判断符号，
# 即大于和小于在没有括号的情况下会比与或要优先判断


# 简单的语句组
# 你也可以在同一行的位置上使用if条件判断语句，如下实例

var = 100

if (var == 100): print "变量 var 的值为100"

print "Good bye!"


