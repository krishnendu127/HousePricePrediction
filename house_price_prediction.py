# -*- coding: utf-8 -*-
"""House_Price_Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYQGNVChUpvT_FVDImgreBBUkLNW1xJf

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

"""importing the boston house price dataset"""

house_price_dataset=sklearn.datasets.fetch_california_housing()

print(house_price_dataset)

# Loading the dataset to a pandas dataframe

house_price_dataframe=pd.DataFrame(house_price_dataset.data, columns=house_price_dataset.feature_names)

print(house_price_dataframe)

#add the target column to the dataframe

house_price_dataframe['price']=house_price_dataset.target

house_price_dataframe.head()

#checking the number of rows and columns in the data frame

house_price_dataframe.shape

#checking for missing values

house_price_dataframe.isnull().sum()

house_price_dataframe.describe()

#understanding the correlation between various features in the dataset

correlation=house_price_dataframe.corr()

#constructing a heapmap to understand the correlation

plt.figure(figsize=(10,10))

sns.heatmap(correlation, cbar=True, square= True, fmt=' .1f', annot=True, annot_kws={'size':8}, cmap='Blues' )

#splitting data and target

X=house_price_dataframe.drop(['price'], axis=1)
Y=house_price_dataframe['price']

print(X)

print(Y)

#splitting data into training data and test data

X_train ,X_test,Y_train, Y_test= train_test_split(X,Y, test_size=0.2, random_state=2 )

print(Y_train)

#model training

model= XGBRegressor()

model.fit(X_train,Y_train)

#evaluation

#accuracy of prediction on train

train_pred=model.predict(X_train)

print(train_pred)

# R squared error

score_1= metrics.r2_score(Y_train, train_pred)

# mean absolute error

score_2= metrics.mean_absolute_error(Y_train, train_pred)

print(score_1)

print(score_2)

#accuracy of prediction on test data

test_pred=model.predict(X_test)

score_3= metrics.r2_score(Y_test, test_pred)
score_4= metrics.mean_absolute_error(Y_test, test_pred)

print(score_3)

print(score_4)

