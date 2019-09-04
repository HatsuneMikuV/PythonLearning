# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fifteen
   Description :
   Author :       joe
   date：          2019-08-13
-------------------------------------------------
   Change Activity:
                   2019-08-13:
-------------------------------------------------
"""

import fourteen


'''
Python 模块
Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

模块让你能够有逻辑地组织你的 Python 代码段。

把相关的代码分配到一个模块里能让你的代码更好用，更易懂。

模块能定义函数，类和变量，模块里也能包含可执行的代码。

import 语句
模块的引入
模块定义好后，我们可以使用 import 语句来引入模块

比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时
模块名.函数名



'''



'''
dir()函数
dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

返回的列表容纳了在一个模块里定义的所有模块，变量和函数
'''


'''
globals() 和 locals() 函数
根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。

如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
'''

'''
reload() 函数
当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块
'''


'''
Python中的包
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包
'''
from runoob.runoobone import runoobone
from runoob.runoobtwo import runoobtwo

if __name__ == '__main__':

    fourteen.printme("123123123")

    print dir(fourteen)
    reload(fourteen)

    runoobone()
    runoobtwo()


    pass