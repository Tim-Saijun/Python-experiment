import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,8,30)
plt.plot(x,3*x**2+7*x-9,"b*")
plt.axis([0,10,-9,260])
plt.xlabel("x的取值")
plt.ylabel("y的值")
plt.title("我是图标题",color="r",fontsize=20)
plt.legend(["我是图例"])
plt.text(5,5,"我是曲线")
plt.show()
