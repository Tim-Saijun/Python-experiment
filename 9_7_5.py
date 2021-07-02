import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,200)
f = x**4+3*x**3+x**2+4*x
f1 = 4*x**3+9*x**2+2*x+4
f2 = 12*x**2+18*x+2
f3 = 24*x+18
plt.plot(x,f,"b-")
plt.axis([-6,6,-20,1400])

plt.subplot(2,2,1)
plt.plot(x,f,"r-")
plt.subplot(2,2,2)
plt.plot(x,f1,"b:")
plt.subplot(2,2,3)
plt.plot(x,f2,"g.")
plt.subplot(2,2,4)
plt.plot(x,f3,"y^")
plt.show()
