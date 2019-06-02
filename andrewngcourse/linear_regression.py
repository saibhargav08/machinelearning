import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plot
import numpy as np



df = pd.read_csv('../datasets/ex1data1.txt', header=None)
df[2] =1
plot.scatter(df[0], df[1], marker='x', color='red')
plot.axis([5, 30, -5, 30])
plot.show()
numpy_data = df.to_numpy()
X = numpy_data[:,[0]]
y = numpy_data[:, [1]]
reg = linear_model.LinearRegression()
reg.fit(X, y)
ypredict = reg.predict(X)
print(reg.coef_)
print(reg.intercept_)
#print(reg.get_params())
x_predict =np.array([[3.5]])
print(reg.predict(x_predict))
print(mean_squared_error(y, ypredict))
plot.scatter(df[0], df[1], marker='x', color='red')
plot.axis([5, 30, -5, 30])
plot.plot(df[0], reg.predict(X), color = 'blue')
plot.xlabel('Population of city in 10,000s')
plot.ylabel('Profit in $10,000s')
plot.show()