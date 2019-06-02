import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv('../datasets/ex1data1.txt', header=None)

X = df.iloc[:,0]
y = df.iloc[:,1]
m = len(y)
plt.scatter(X, y)
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.show()
X = X[:, np.newaxis]
y= y[:, np.newaxis]
theta = np.zeros([2, 1])
iterations = 1500
alpha = 0.01
ones = np.ones((m, 1))
X =  np.hstack((ones, X))

def computecost(X, y, theta):
    temp = np.dot(X, theta) - y
    return np.sum(np.power(temp, 2))/2*m
J = computecost(X, y, theta)
print(J)

def gradientDescent(X, y, theta, alpha, iterations):
    for _ in range(iterations):
        temp = np.dot(X, theta) - y
        temp = np.dot(X.T, temp)
        theta = theta - (alpha/m) * temp
    return theta
theta = gradientDescent(X, y, theta, alpha, iterations)
print(theta)
J = computecost(X, y, theta)
print(J)


plt.scatter(X[:,1], y)
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.plot(X[:,1], np.dot(X, theta))
plt.show()
