def inlist(a): #'输入名单'用的函数
    b = set(a.split(','))
    return b
m100 = inlist(input('输入100m名单'))
m200 = inlist(input('输入200m名单'))
m400 = inlist(input('输入400m名单'))
print(((m100&m200)|(m100&m400)|(m200&m400))-(m100&m200&m400))

