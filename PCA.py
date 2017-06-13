#PCA
#https://www.analyticsvidhya.com/blog/2016/03/practical-guide-principal-component-analysis-python/

import os
os.chdir('C:/Dentsu/Code 1 Infinity/Infinity Reboot/codes/test')

import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
#%matplotlib inline

#Load data set
data = pd.read_csv('data/Big_Mart_PCA.csv')
data_col = data.columns
#Now we are left with removing the dependent (response) variable and other identifier variables( if any). As we said above, we are practicing an unsupervised learning technique, hence response variable must be removed.
data_col = data_col.drop({'Item_Identifier','Outlet_Identifier','Item_Outlet_Sales'})
subdata = data[data_col]

#imputed missing values
Item_Weight_median = subdata['Item_Weight'].median()
subdata['Item_Weight'] = subdata['Item_Weight'].fillna(Item_Weight_median)

subdata['Outlet_Size'] = subdata['Outlet_Size'].fillna('other')

Item_Visibility_median = subdata['Item_Visibility'].median()
subdata['Item_Visibility'] = subdata['Item_Visibility'].map(lambda x: Item_Visibility_median if x ==0 else x)

#one hot encoding to convert categorical variable to numbers
one_hot = pd.get_dummies(subdata)
#convert it to numpy arrays
X=one_hot.values
#X=subdata.values
print X[:3]
#Scaling the values, string cannot call the function
X = scale(X)
#the function Standardize a dataset along any axis. Center to the mean and component wise scale to unit variance.

pca = PCA(n_components=35)

pca.fit(X)

#The amount of variance that each PC explains
var= pca.explained_variance_ratio_

#Cumulative Variance explains
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

print var1
#[ 10.22  17.04  23.13  28.42  33.3   36.97  40.32  43.57  46.72  49.85
#  52.95  56.    59.02  62.02  65.01  67.94  70.85  73.71  76.56  79.4   82.2
#  84.96  87.69  90.26  92.76  95.02  97.23  99.25  99.68  99.97  99.99
#  99.99  99.99  99.99  99.99]

plt.plot(var1)

#Looking at above plot I'm taking 30 variables
pca = PCA(n_components=30)
pca.fit(X)
X1=pca.fit_transform(X)

print X1