from datetime import *
ti = datetime.now()
print(ti.strftime('%Y-%m-%d'))
print(ti.strftime('%m-%d-%Y'))
print(ti.strftime('%Y-%d-%m'))
if ti.month == 1 or 2 or 3:
    sta = '当前第一季度'
elif ti.month == 4 or 5 or 6:
    sta = '当前第二季度'
elif ti.month == 7 or 8 or 9:
    sta = '当前第三季度'
elif ti.month == 10 or 11 or 12:
    sta = '当前第四季度'
print(sta)
