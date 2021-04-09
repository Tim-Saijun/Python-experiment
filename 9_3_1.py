w = eval(input("请输入行李重量/kg ： \n"))
if w > 50:
    y = (w-50)*0.35+50*0.25
elif w >= 0:
    y = w*0.25
else:
    y = '请检查输入值！'
print('行李托运费',y,'元')
