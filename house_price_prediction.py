# -*- coding: utf-8 -*-
"""House Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WE1-ybL3aUod1xsRegzbE5Yif-kVCEu9

Importing the dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

dataset=sklearn.datasets.load_boston()

print(dataset)

#Loading the dataset into a pandas dataframe
house_price=pd.DataFrame(dataset.data,columns=dataset.feature_names)

house_price

house_price.head()

#add the target column to the dataframe
house_price['price']=dataset.target

house_price.head()

# check the number of rows and columns in the dataframe
house_price.shape

#check for missing values
house_price.isnull().sum()

#statistical measures of dataset
house_price.describe()

"""Understaning the correlation between various features in the dataset"""

correlation=house_price.corr()

#constructing a heatmap to understand correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True,fmt='.if',annot=True,annot_kws={'size':8},cmap='Blues')

"""Splitting the data and target"""

X=house_price.drop(['price'],axis=1)
Y=house_price['price']

print(X)
print(Y)

"""Spillting the data into trainingdata and testing data"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Model Training

XGBoost Regressor
"""

#load the model
model=XGBRegressor()

#training the model with X_train
model.fit(X_train,Y_train)

"""Evaluation

Prediction on training data
"""

#accuracy for prediction on training data
training_data=model.predict(X_train)

print(training_data)

# R squared error
score1=metrics.r2_score(Y_train,training_data)

# Mean absolute Error
score2=metrics.mean_absolute_error(Y_train,training_data)
print("R Squared Error",score1)
print("mean absolute error",score2)

#Visualizing the actual price and preicte prices
plt.scatter(Y_train,training_data)
plt.xlabel("Actual price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Price")
plt.show()

test_data=model.predict(X_test)

# R squared error
score1=metrics.r2_score(Y_test,test_data)

# Mean absolute Error
score2=metrics.mean_absolute_error(Y_test,test_data)
print("R Squared Error",score1)
print("mean absolute error",score2)

#Visualizing the actual price and preicte prices
plt.scatter(Y_test,test_data)
plt.xlabel("Actual price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Price")
plt.show()

