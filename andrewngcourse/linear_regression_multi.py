import torch as th
import numpy as np
import matplotlib.pyplot as plt

x, y, z = np.loadtxt('../datasets/ex1data2.txt', delimiter=',', unpack=True, usecols =(0, 1, 2))
# x - size of houses in square feet
# y - no of bedrooms
# z  - housing prices
plt.plot(x, z,'ro', color='red')
plt.xlabel('Size of houses in Square feet')
plt.ylabel('Housing prices')
plt.title('Size of houses in Square feet vs Housing prices')
plt.show()

plt.plot(y, z,'ro', color='red')
plt.xlabel('No of bedrooms')
plt.ylabel('Housing prices')
plt.title('No of bedrooms vs Housing prices')
plt.show()


X =th.tensor(np.vstack((np.ones(np.shape(x)), x, y)))
theta =th.mm(th.mm(th.inverse(th.mm(X, X.t())), X), th.tensor([z]).t())
z_predict = th.mm(theta.t(), X).t().numpy()
print(z- z_predict)