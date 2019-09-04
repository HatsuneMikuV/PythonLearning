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
   # 为了执行下面的代码   强行中端循环
   break

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

# 无线循环 导致下面的代码不能执行，因此注释
# while (flag): print 'Given flag is really true!'

print "Good bye!"


# Python for 循环语句
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串

for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit

# 通过序列索引迭代
# 另外一种执行循环的遍历方式是通过索引
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

print "Good bye!"

# 以上实例我们使用了内置函数 len() 和 range(),
# 函数 len() 返回列表的长度，即元素的个数。
# range返回一个序列的数。

# 循环使用 else 语句
# 在 python 中，for … else 表示这样的意思，
# for 中的语句和普通的没有区别，
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
# while … else 也是一样

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
   for i in range(2, num): # 根据因子迭代
      if num % i == 0:      # 确定第一个因子
         j = num / i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num, i, j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'


# Python 循环嵌套
# Python 语言允许在一个循环体里面嵌入另一个循环
# 你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环
# 反之，你可以在for循环中嵌入while循环

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1


# Python break 语句
# Python break语句，就像在C语言中，打破了最小封闭for或while循环。
# break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
# break语句用在while和for循环中。
# 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    print '当前变量值 :', var
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break

# Python continue 语句
# Python continue 语句跳出本次循环，而break跳出整个循环。
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句用在while和for循环中

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值 :', var

# 只打印0-10之间的奇数，可以用continue语句跳过某些循环

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print n

# Python pass 语句
# Python pass 是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句

# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

# 在 Python 中有时候会看到一个 def 函数:

def sample(n_samples):
    pass
# 该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，
# 当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。
