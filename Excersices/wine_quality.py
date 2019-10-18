import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model


df1 = pd.read_csv('../datasets/winequality-red.csv', delimiter=';')
df2 = pd.read_csv('../datasets/winequality-white.csv', delimiter=';')
df = pd.concat([df1, df2])
X = df.iloc[:,:-1]
y = df.iloc[:,11]
m = len(y)
# plt.scatter(X, y)
# plt.xlabel('Fixed acidity')
# plt.ylabel('Quality of wine')
# plt.show()

model_object = linear_model.LinearRegression()
model = model_object.fit(X, y)
Y= (model_object.predict(X))
Y = Y.round()
print(model.score(X, Y))
print(model_object.coef_)
print(model_object.intercept_)