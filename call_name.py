import module_name
import module_math

name = input("Enter a name")
module_name.display(name)

print(dir(module_name))

print("\n")

print(dir(module_math))


from module_math import add

a= 10
b = 42

print('sum is',add(a,b))

from module_math import *

print('mul is', mul(a,b))
