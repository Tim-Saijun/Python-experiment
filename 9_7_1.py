import numpy as np
x = np.array(([1,2,3],
              [4,5,6],
              [7,8,9]))
print(x.sum())
print(x.mean(axis= 1))
print(x.mean(axis= 0))
