def prime(x):
    if x == 1:
            return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
    return True
        
def pro(x):
    if x<4 and x%2 != 0:
        print("无效输入！")
    else :
        printcount = 0
        for i in range(2,x):
            if prime(i) == 1 and prime(x-i) == 1:
                    if printcount % 6 == 0 and printcount != 0:
                        print("\n%d=%d+%d"%(x,i,x-i),end=' ')
                        printcount += 1
                    else:
                        print("%d=%d+%d"%(x,i,x-i),end=' ')
                        printcount += 1
pro(648)
