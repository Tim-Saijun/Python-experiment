vote = [4,7,8,1,2,2,6,2,2,1,6,8,7,4,5,5,5,8,5,5,4,2,2,6,4]
ans1 = list(set(vote))
ans2 = set(ans1[0:3])
ans3 = set(ans1[4:7])
print(set(ans1))
print(set(ans1)&ans2)
print(ans3 - set(ans1))
if vote.count(int(input('输入要查询的候选人编号：'))) != 0:
    sta = True
else:
    sta = False
print(sta)
