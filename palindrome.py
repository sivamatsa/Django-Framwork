'''#random number (1,120) ,, IMPLIMENT PALINDROME

import math
import random

#n = random.randint(100,999)
#str(n)
#print(n.split())
#n.split()
#print(n[:])
n = int(input("Enter a Number"))

try:
    val = int(num)
    
        if n == str(n[::-1]):
            print("palindrome")

        else:
            print("Not a Palindrome")

'''

class Palindrome:
    def randomNum(N,lb,ub):
        import random
        res = [random.randint(lb,ub+1) for i in range(N)]
        return res

    def ispalindrome(S):
        if(S==S[::-1]):
            return True
        else:
            return False
