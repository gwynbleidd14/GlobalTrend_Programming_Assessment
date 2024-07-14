'''
3. Write a Python script that trains a simple linear regression model using scikit-learn. Use
a dataset of your choice, split it into training and testing sets, and evaluate the model's
performance.
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset =  pd.read_csv("D:\Desktop\Global Trend Assignment\Assessment\salary.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)
print("\n")
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)
print("Training data:")
print(X_train)
print(y_train)
print("\n")
print("Test data:")
print(X_test)
print(y_test)
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
print("Predicted values:", y_pred)
print("Actual values:", y_test)
