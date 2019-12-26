# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_12
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/26
-------------------------------------------------
   Change Activity:  2019/12/26:
-------------------------------------------------
"""

'''
Container With Most Water
'''

'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

def maxArea_test(numbers):
    if len(numbers) < 2:
        return 0
    result = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                result = max(result, numbers[i] * (j - i))
            else:
                result = max(result, numbers[j] * (j - i))
    return result

def maxArea(numbers):
    result = 0
    if len(numbers) < 2:
        return result
    count = len(numbers)
    left = 0
    right = count - 1
    while left < right:
        if numbers[left] < numbers[right]:
            result = max(result, numbers[left] * (right - left))
            left += 1
        else:
            result = max(result, numbers[right] * (right - left))
            right -= 1
    return result

if __name__ == '__main__':

    l = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print maxArea(l), maxArea_test(l)

    pass