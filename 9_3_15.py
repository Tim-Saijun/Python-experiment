s = 0
l = [1,2,3]
while s <= 2000 :
    s = l[-1] + l[-2] + l[-3]
    l.append(s)
    print(l)
print('该数列从第%d项开始，其数值超过2000.'%(l.index(s)+1))
