import torch as th
import numpy as np
import matplotlib.pyplot as plt



x, y = np.loadtxt('../datasets/ex1data1.txt', delimiter=',', unpack=True, usecols =(0, 1, ))

plt.plot(x, y,'ro', color='blue')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.title('Population vs profit ')
plt.show()
x_ = np.vstack((np.ones(np.shape(x)), x))
X =th.tensor(x_)
y_ = th.tensor([y])
transpose = X.t()
z =th.mm(th.mm(th.inverse(th.mm(X, transpose)), X), y_.t())
y_predict = th.mm(z.t(), X).t().numpy()
plt.plot(x, y,'ro', color='blue')
plt.plot(x, y_predict)
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.title('Population vs profit ')
plt.show()


