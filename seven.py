# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     seven
   Description :
   Author :       joe
   date：          2019-07-23
-------------------------------------------------
   Change Activity:
                   2019-07-23:
-------------------------------------------------
"""

# Python 循环语句

# 循环语句允许我们执行一个语句或语句组多次
# Python提供了for循环和while循环（在Python中没有do..while循环）

'''
循环类型	            描述
while 循环	        在给定的判断条件为 true 时执行循环体，否则退出循环体。
for 循环	            重复执行语句
嵌套循环	            你可以在while循环体中嵌套for循环
'''

# 循环控制语句
# 循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句

'''
控制语句	            描述
break 语句	        在语句块执行过程中终止循环，并且跳出整个循环
continue 语句	    在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句	        pass是空语句，是为了保持程序结构的完整性。
'''

#  xrange  0 - 7
for i in xrange(8):
    print i


smaller_solutions = [[[1, 4]], [[2, 5]]]
for solution in smaller_solutions:
    print solution
    for r, c in reversed(solution):
        print r, c

print [(1, 1)] + [(2, 2)]

print "========================================"
#  * queen problem with recurison
BOARD_SIZE = 8

def under_attack(col, queens):
   left = right = col
   for r, c in reversed(queens):
        #  左右有冲突的位置的列号
       left, right = left - 1, right + 1

       if c in (left, col, right):
           return True
   return False

def solve(n):
   if n == 0:
       return [[]]

   smaller_solutions = solve(n - 1)
   return [solution + [(n, i+1)]
            for i in xrange(BOARD_SIZE)
                for solution in smaller_solutions
                    if not under_attack(i+1, solution)]

for answer in solve(BOARD_SIZE):
   print answer
   print "----------------------------------------"



print "========================================"
#  找出排序数组的索引
def deduplication(self, nums):
    for i in range(len(nums)):
        if nums[i] == self:
            return i
    i = 0
    for x in nums:
        if self > x:
            i += 1
    return i

print deduplication(5, [1,3,5,6])


# Python While 循环语句
# Python 编程中 while 语句用于循环执行程序，
# 即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务

count = 0
while count < 9:
   print 'The count is:', count
   count = count + 1

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print even, odd, numbers

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
# continue 用于跳过该次循环，
# break 则是用于退出循环，
# 此外"判断条件"还可以是个常值，表示循环必定成立

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# 无限循环
# 如果条件判断语句永远为 true，循环将会无限的执行下去

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num
   if int(num) == 1001: break

print "Good bye!"


# 循环使用 else 语句
# 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"



# 简单语句组
# 类似 if 语句的语法，
# 如果你的 while 循环体中只有一条语句，
# 你可以将该语句与while写在同一行中

flag = 1

while (flag): print 'Given flag is really true!'

print "Good bye!"