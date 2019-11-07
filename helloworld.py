# -*- coding:utf-8 -*-
print("Hello,world !")
import keyword
import time

n = 0
"""
for i in keyword.kwlist:
    time.sleep(3)
    print(i)
    n += 1
    print(n)
"""
for s in "python":
    if s == "t":
        continue
    print(s, end="")
print("\n","区分continue与 break")
for s in "python":
    if s == "t":
        break
    print(s, end="")


lista = ("False, None, True, and, as, assert, async, await, break, class, continue, def,"
         "del, elif, else, except, finally, for, from, global, if, import, in, is, lambda,"
         "nonlocal, not, or, pass, raise, return,try, while, with, yield ")
