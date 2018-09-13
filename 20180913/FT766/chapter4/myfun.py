# -*- coding: utf-8 -*-
"""
關於這個腳本的註解寫在這裡
"""

import math

def myfun(x, y):
    """ 自訂的函式 """
    a = math.cos(3 * (x - 1)) + \
      math.sin(3 * (y - 1))
    return a

# 測試使用定義的函式
x, y = 2.0, 5.0
print("myfun(x, y) = %f" % myfun(x, y))

def myfunc(n, b):
    x = n % b
    if x == 0:
        return 1
    else:
        return 0

n = 123456
b = 3

myfunc(n, b)
