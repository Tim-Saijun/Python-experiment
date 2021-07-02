#统计字符频率
def count_num(string):
    ls = string.split(' ')
    se = set(ls)
    di = {}
    for word in se:
        di[word] =  ls.count(word)
    return di
S1 = "Python VB VFP C C++ Java Python Python C"
dic = count_num(S1)
for key,value in sorted(dic.items(),reverse=1):
    print(key,value)
