import random
for i in range(100,1000): 
    j = str(i)
    if int(j[0:1])**3+int(j[1:2])**3+int(j[2:3])**3 == i :
        print(i,end=',')
