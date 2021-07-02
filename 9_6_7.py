f = open("sy6-7.txt","r")
contalist = f.read().split("\n")
contadic={}
for pep in contalist:
    peplist = pep.split(",")
    contadic[peplist[0]] = peplist[1]
f.close()
nam = input("Input Name:  ")
if nam in contadic:
    print(contadic[nam])
else:
    print("查无此人")
