scores = []
for i in range(0,10):
    scores.append(int(input('输入评分')))
print('十位评委给分为：',scores)
scores.remove(max(scores))
scores.remove(min(scores))
print('最终得分为：',sum(scores)/len(scores))
