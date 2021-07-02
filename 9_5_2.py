import math
import random
def mulprime(x,y):
    if math.gcd(x,y) == 1:
        flag = True
    else:
        flag = False
    print(flag,(x,y))
mulprime(random.randint(0,100),random.randint(0,100) )
