
for x in range(3,1001):
    sum = 0 #因子和的初始值
    for i in range(1,x):
        if x%i == 0 :
            sum += i
    if x == sum:
            print(x)
print('以上为1-1000所有完美数。')
