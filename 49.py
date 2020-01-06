# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        49
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/6
-------------------------------------------------
   Change Activity:  2020/1/6:
-------------------------------------------------
"""


'''
题目：两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。
有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''


if __name__ == '__main__':

    print "c -- y"
    print "a -- z"
    print "b -- x"

    pass

a = 0
b = 0
c = 0
while (a == 0 or b == 0 or c == 0):
    for i in range(ord('x'), ord('z') + 1):
        if i != ord('x') and i != ord('z'):
            c = i
        if i != ord('x') and c > 0 and c != i:
            a = i
        if a > 0 and c > 0 and c != i and a != i:
            b = i

print "a -- %s  b -- %s  c -- %s" % (chr(a), chr(b), chr(c))

for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            for k in range(ord('x'), ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print 'order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k))