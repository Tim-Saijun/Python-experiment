n = int(input('请输入正整数n： '))
s = 0
for i in range(0,n+1):
    j = i
    for k in range(0,j+1):
         s = s + k
print(s)
