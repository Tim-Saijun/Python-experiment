import jieba
f = open("sy6-8.txt","r")
po = f.read()
words = jieba.lcut(po)
wodic = {}
for wo in words:
    wodic[wo] = words.count(wo)
ans = sorted(wodic.items(),key = lambda x:x[1],reverse=1)
i = 0
while i<=4:
        print(ans[i][0],ans[i][1])
        i += 1
