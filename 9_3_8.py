for i in range(1,1001):
    a = str(i)
    b = str(i**2)
    l = len(a)
    if b.endswith(a,-1-l) == True:
        print(i)
print('1-1000同构数如上。')
