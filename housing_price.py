# -*- coding: utf-8 -*-
"""Housing Price.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N9FeL1HC8xcmvYFxp9a5H1hflQl2WORW
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("/content/housing.csv")
data.head()

data.info()

data.dropna(inplace=True)

data.info()

from sklearn.model_selection import train_test_split
x=data.drop(['median_house_value'],axis=1)
y=data['median_house_value']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

train_data=x_train.join(y_train)
train_data

train_data.hist(figsize=(15,8))

plt.figure(figsize=(15,8))
sns.heatmap(train_data.drop('ocean_proximity', axis=1).corr(),annot=True,cmap='YlGnBu')

train_data['total_rooms']=np.log(train_data['total_rooms']+1)
train_data['total_bedrooms']=np.log(train_data['total_bedrooms']+1)
train_data['population']=np.log(train_data['population']+1)
train_data['households']=np.log(train_data['households']+1)
train_data.hist(figsize=(15,8))

train_data=train_data.join(pd.get_dummies(train_data.ocean_proximity)).drop(['ocean_proximity'],axis=1)

train_data

plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(),annot=True,cmap='YlGnBu')

plt.figure(figsize=(15,8))
sns.scatterplot(x="latitude",y="longitude",data=train_data,hue="median_house_value",palette="coolwarm")

train_data['bedroom_ratio']=train_data['total_bedrooms']/train_data['total_rooms']
train_data['household_rooms']=train_data['total_rooms']/train_data['households']

plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(),annot=True,cmap='YlGnBu')

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x_train,y_train=train_data.drop(['median_house_value'],axis=1),train_data['median_house_value']
x_train_s=scaler.fit_transform(x_train)
reg=LinearRegression()
reg.fit(x_train_s,y_train)

test_data=x_test.join(y_test)
test_data['total_rooms']=np.log(test_data['total_rooms']+1)
test_data['total_bedrooms']=np.log(test_data['total_bedrooms']+1)
test_data['population']=np.log(test_data['population']+1)
test_data['households']=np.log(test_data['households']+1)

test_data=test_data.join(pd.get_dummies(test_data.ocean_proximity)).drop(['ocean_proximity'],axis=1)


test_data['bedroom_ratio']=test_data['total_bedrooms']/test_data['total_rooms']
test_data['household_rooms']=test_data['total_rooms']/test_data['households']

x_test,y_test=test_data.drop(['median_house_value'],axis=1),test_data['median_house_value']

x_test_s=scaler.transform(x_test)
reg.score(x_test_s,y_test)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()
rf.fit(x_train_s,y_train)

rf.score(x_test_s,y_test)

from sklearn.model_selection import GridSearchCV
rf=RandomForestRegressor()
param_grid={
    'n_estimators':[100,200,300],
    'min_samples_split':[2,4],
    'max_depth':[None,4,8]
}
gs=GridSearchCV(rf,param_grid,cv=5,
                scoring='neg_mean_squared_error',
                return_train_score=True)
gs.fit(x_train_s,y_train)

best_forest=gs.best_estimator_
gs.best_estimator_.score(x_test_s,y_test)

