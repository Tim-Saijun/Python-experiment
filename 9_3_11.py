sum = 2
for x in range(3, 101):
    for i in range(2, x):
        if x%i == 0 :
            break
        else:
            sum += x
print('一百以内素数之和为',sum)

