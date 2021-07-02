import pandas as pd
df = pd.read_excel("d:\\stu.xlsx")
print(df)
print(df.loc[(df["语文成绩"]<60)|(df["数学成绩"]<60)|(df["英语成绩"]<60)])
clas = df.groupby("班级")
print(clas.mean())
