s = input('按先后顺序输入姓名，以逗号分隔：')
nam =s.split(',')
nam.insert(0,'Actors')
print(nam.index(input('要查询的同学姓名')))
