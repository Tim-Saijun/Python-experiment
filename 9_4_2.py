import random as r
b = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
for i in range(10) :
      print(b[r.randint(0,61)],b[r.randint(0,61)],b[r.randint(0,61)],b[r.randint(0,61)],b[r.randint(0,61)],b[r.randint(0,61)],b[r.randint(0,61)],b[r.randint(0,61)],end='\n')  #随机生成的8位密码
