#find even or odd with use of packages

num = int(input("Enter a Number"))

if((num%2) == 0):
    print(num,"is Even Number")

else:
    print(num,"is Odd Number")


print("\n")

import random
i = random.randrange(100)
if i%2==0:
    print('even',i)
else:
    print('odd',i)

i = random.randrange(100)
if i%2!=0:
    print('odd',i)
else:
    print('even',i)

import math
print(math.floor(4))
    
