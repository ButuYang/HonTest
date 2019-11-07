# -*- coding:utf-8 -*-
print("Hello,world !")
import keyword
import time
for i in keyword.kwlist:
    time.sleep(3)
    print(i)

lista = ("False, None, True, and, as, assert, async, await, break, class, continue, def,"
         "del, elif, else, except, finally, for, from, global, if, import, in, is, lambda,"
         "nonlocal, not, or, pass, raise, return,try, while, with, yield ")
