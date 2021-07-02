scores = [30,50,20,57,70,100,90]
good = [] #成绩为优
bad = []    #成绩不及格
for x in scores :
    if x >= 90:
        good.append(x)
    elif x < 60:
        bad.append(x)
print('成绩为优 的平均分为：',sum(good)/len(good))
print('成绩不及格 的平均分为：',sum(bad)/len(bad))
