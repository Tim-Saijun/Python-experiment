import random
a = ''
while a  != 'quit':
  x = random.randint(0,9)
  y = random.randint(0,9)
  a = str(input('%d + %d =  '%(x,y)))
  b = eval(a)
  if b == x + y:
    print('计算正确')
  if a == 'quit':
      break
  else :
    print('计算错误')
    
