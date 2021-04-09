import math
x = eval(input('请输入e的指数x：'))
l = [1]                         #l这个列表用来存放多项式的每一项
n = 2
while (x**n)/math.factorial(n) >= pow(10,-6) :
     an = (x/(n-1))*l[-1]   #泰勒公式前后项递推关系
     l.append(an)
     n += 1
     print(l)
else:
    print('e^x=',sum(l))
