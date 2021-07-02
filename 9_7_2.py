import numpy as np
x = np.random.rand(5,5)
a = (np.array(x)-x.min())/(x.max()-x.min())
print(a)
