scores = {'Han':65,'Wang':97,'Ma':73,'Xu':85,'Yang':92,'a':97}
scores_list = sorted((scores.values()),reverse=1)
for i in range (0,len(scores_list)):
    for (name,mark) in scores.items():
        if mark == scores_list[i] :
            print(name)
