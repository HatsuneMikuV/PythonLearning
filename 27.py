# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        27
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/10/8
-------------------------------------------------
   Change Activity:  2019/10/8:
-------------------------------------------------
"""

'''
Python JSON
本章节我们将为大家介绍如何使用 Python 语言来编码和解码 JSON 对象。

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。

JSON 函数
使用 JSON 函数需要导入 json 库：import json。

函数	描述
json.dumps	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象

json.dumps
json.dumps 用于将 Python 对象编码成 JSON 字符串。

语法
json.dumps(obj, skipkeys=False, ensure_ascii=True, 
check_circular=True, allow_nan=True, cls=None, indent=None, 
separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)

'''

'''
python 原始类型向 json 类型的转化对照表：

Python	JSON
dict	object
list, tuple	array
str, unicode	string
int, long, float	number
True	true
False	false
None	null
json.loads
json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

语法
json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])


json 类型转换到 python 的类型对照表：

JSON	Python
object	dict
array	list
string	unicode
number (int)	int, long
number (real)	float
true	True
false	False
null	None

'''

import json


'''

使用第三方库：Demjson
Demjson 是 python 的第三方模块库，可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能。

JSON 函数
函数	描述
encode	将 Python 对象编码成 JSON 字符串
decode	将已编码的 JSON 字符串解码为 Python 对象
encode
Python encode() 函数用于将 Python 对象编码成 JSON 字符串。

decode
Python 可以使用 demjson.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。

语法
demjson.decode(self, txt)

'''
import demjson


if __name__ == '__main__':
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    jsons = json.dumps(data)
    print jsons

    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    text = json.loads(jsonData)
    print text

    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json = demjson.encode(data)
    print json

    json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
    text = demjson.decode(json)
    print  text

    pass