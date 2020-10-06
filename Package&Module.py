'''

package : like  a folder
    Collections of madules

Module:
    set of functions or programe for specific task

    access with import module name
    from modulename import class

    '''
import keyword
print(dir(keyword))
print("\n")
print(keyword.kwlist)
print("\n")
import math
print(dir(math))
print("\n")
print(math.factorial(27))
print("\n")
print(math.sqrt(999))
print("\n")
print(math.sin(23))
print("\n")

import time

print(dir(time))
print("\n")
print(time.ctime())
print("\n")
time.sleep(5)
print("its sleeping time",time.ctime())
time.sleep(10)
print("\n")
print(time.ctime())
