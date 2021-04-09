a,b,c = eval(input('输入三角形三边长，连续输入并以逗号隔开：  '))
if a  <= 0 or b  <= 0 or c  <= 0 :
    print('数据不合法！')
elif a+b <= c or a+c <= b or c+b <= a:
    print('不能构成三角形！')
else :
    import math as m
    h = (a+b+c)/2
    s = m.sqrt(h*(h-a)*(h-b)*(h-c))
    print('三角形面积为:',format(s,'.2f'))
    
