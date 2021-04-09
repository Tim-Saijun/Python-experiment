salary = eval(input('输入工资/元 ：  '))
if salary <= 400:
    f = 0.005 * salary
elif salary <= 600:
    f = 0.01 *salary
elif salary <= 800:
    f = 0.015 * salary
elif salary <= 1500:
    f = 0.02 * salary
elif salary > 1500:
    f = 0.03 * salary
else:
    f = 'null'
print('应交党费',format(f,'.2f'),'元。')
