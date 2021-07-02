def f(n):
    lst=[]
    j = 1
    while sum(lst) != n**3:
        lst = list(range(j,j+2*n,2))
        j += 1
    return lst
