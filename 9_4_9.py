code = {'user1':'abcd','i':'0000'}
i = 1
while 1:
  user = input('User Name: ')
  pas = input('Password: ')
  if code.get(user) == pas :
      print('Welcome!')
      break
  elif i != 3:
      print('Please Retry!')
      i += 1
  else :
       print('次数用尽，无法登陆。')
       
