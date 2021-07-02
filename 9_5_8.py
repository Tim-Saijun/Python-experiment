def isSymmetrical(x):
    for i in range(4):
        for j in range(4):
            if x[i][j] != x[j][i]:
                return False
    return True

def prime(x):
    if x == 1:
            return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
    return True
if __name__ == "__main__":
    x = list(input("输入矩阵元素"))
    if isSymmetrical(x)==1:
        print("The matrix is symmetrical.")
    else:
        print("The matrix is not symmetrical.")
    if prime(x) == 1:
        for i in x:
            count = 0
            if prime(i) == 1:
                count += 1
        print("The number has %d prime numbers."%count)
