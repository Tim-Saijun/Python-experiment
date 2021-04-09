for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
              if (a*1000 + b*100 + c*10 + d*1) - (c*100 + d*10 + c*1) == (a*100 + b*10 +c*1):
                   print('满足ABCD - CDC = ABC的A、B、C、D的值分别为：',a,b,c,d)
