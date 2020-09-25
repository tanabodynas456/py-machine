import numpy as np
import matplotlib.pyplot as plt
rng = np.random
x=rng.rand(50)*10
b=rng.randn(50)
y=2*x+b
print(y)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph y=2*x+b")
plt.grid()
plt.show()
#y=ax+b