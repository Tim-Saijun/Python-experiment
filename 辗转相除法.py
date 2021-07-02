#辗转相除法
def gcd(x,y):
    r = x % y
    if r == 0:
        return y
    else:
        return gcd(y,x%y)
print(gcd(66,7777))
import random
def mulprime(x,y):
    if gcd(x,y) == 1:
        flag = True
    else:
        flag = False
    print(flag,(x,y))
mulprime(7,6) 
mulprime(random.randint(0,100),random.randint(0,100) )
