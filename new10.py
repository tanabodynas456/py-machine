import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
rng = np.random
#การจำลองข้อมูล #y=ax+b
x=rng.rand(50)*10
b=rng.randn(50)
y=2*x+b
#linear regression model
model=LinearRegression()
print(x)
x_new = x.reshape(-1,1)
print(x_new)
#train
model.fit(x_new,y)
print(model.score(x_new,y))
print(model.intercept_)
print(model.coef_)
#test model
xfit=np.linspace(-1,11)
print(xfit)
xfit_new=xfit.reshape(-1,1)
print(x_new)
yfit=model.predict(xfit_new)
#analysis model & result
plt.scatter(x,y)
plt.plot(xfit,yfit)
plt.show()