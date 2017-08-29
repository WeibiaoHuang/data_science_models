
# coding: utf-8

# In[1]:

import os
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import cross_validation, metrics
import xgboost


# ## Exploratory Analysis

# In[2]:

os.chdir('C:/Dentsu/Code 1 Infinity/Infinity Reboot/codes/test')
data = pd.read_csv('data/Uber Marketing Analyst DriverData.csv')
data.head(10)
# data.describe()


# In[3]:

data.shape


# In[4]:

def _exploratory_analysis_string(column_name):
    num_null = data[column_name].isnull().sum()
    print 'Number of Missing values for '+column_name+': %d'%num_null
    print 'Frequency Table for '+column_name+' :' 
    return data[column_name].value_counts()


# In[5]:

_exploratory_analysis_string('city_name')


# In[6]:

_exploratory_analysis_string('signup_os')


# In[7]:

_exploratory_analysis_string('signup_channel')


# In[8]:

_exploratory_analysis_string('vehicle_make')


# In[9]:

_exploratory_analysis_string('vehicle_model')


# Here we assume all the model is the correct input (as we observe 5-Sep, which might be some error input). It could be further improved by cross-validating against external data sources.

# In[10]:

# Example for Histogram
import matplotlib.pyplot as plt
temp1 = data['signup_channel'].value_counts(ascending=True)
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('SignUp_Channel')
ax1.set_ylabel('Count of SignUp')
ax1.set_title("Signup by Channel")
temp1.plot(kind='bar')
plt.show()


# ## Input Data Encoding

# #### Check Month for Datetime Binning

# In[11]:

def _check_month(column_name):
    num_null = data[column_name].isnull().sum()
    print 'Number of Missing values for '+column_name+': %d'%num_null
    temp_month = data[column_name][data[column_name].notnull()].apply(lambda x: x.split('/')[0])
    print('Frequency Table for Month of '+column_name)
    return temp_month.value_counts()


# In[12]:

_check_month('signup_date')


# In[13]:

_check_month('bgc_date')


# In[14]:

_check_month('vehicle_added_date')


# #### Binning the Datetime

# In[15]:

# Date Binning based on every ten days
data['signup_date'] = data['signup_date'][data.signup_date.notnull()].apply(lambda x: int(x.split('/')[1]))
bins = [1, 10, 20, 31]
group_names = ['first_10d', 'middle_10d', 'last_10d']
data['signup_date'] = pd.cut(data['signup_date'], bins, labels=group_names)


# In[16]:

def _datetime_binning_on_Month(column_name):
    data[column_name] = data[column_name][data[column_name].notnull()].apply(lambda x: x.split('/')[0])
    print('Datetime successfully binned for '+column_name)
    
_datetime_binning_on_Month('bgc_date')
_datetime_binning_on_Month('vehicle_added_date')


# In[17]:

data.head(20)
# data.shape


# #### One Hoc Encoding

# In[18]:

encode_list = ['city_name', 'signup_os', 'signup_channel', 'signup_date', 'bgc_date', 'vehicle_added_date', 'vehicle_make', 'vehicle_model', 'vehicle_year']
def one_hoc_encoder(data, column_list):
    for column in column_list:
        data = pd.get_dummies(data, prefix=column, columns=[column])
    return data
data = one_hoc_encoder(data, encode_list)


# In[19]:

data.columns


# In[20]:

# assuming all the null in "first_completed_date" are those not complete the first drive, but not missing value
data.first_completed_date = data.first_completed_date.isnull()


# In[21]:

data.head(20)


# ## Modeling

# In[22]:

train, test = train_test_split(data, test_size = 0.3)
x_train = train.drop(['id', 'first_completed_date'], axis = 1)
y_train = train.first_completed_date
x_test = test.drop(['id', 'first_completed_date'], axis = 1)
y_test = test.first_completed_date
print x_train.shape
print y_train.shape
print x_test.shape
print y_test.shape


# In[23]:

# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import PolynomialFeatures, StandardScaler
# from sklearn.svm import LinearSVC
# polynomial_svm_clf = Pipeline((
#         ("poly_features", PolynomialFeatures(degree=10)),
#         ("scaler", StandardScaler()),
#         ("svm_clf", LinearSVC(C=10, loss="hinge"))
#     ))
# polynomial_svm_clf.fit(x_train, y_train)


# In[26]:

def modelfit(alg, dtrain, predictors,useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
    
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(dtrain[predictors].values, label=dtrain[target].values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
            metrics='auc', early_stopping_rounds=early_stopping_rounds, show_progress=False)
        alg.set_params(n_estimators=cvresult.shape[0])
    
    #Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain['Disbursed'],eval_metric='auc')
        
    #Predict training set:
    dtrain_predictions = alg.predict(dtrain[predictors])
    dtrain_predprob = alg.predict_proba(dtrain[predictors])[:,1]
        
    #Print model report:
    print "\nModel Report"
    print "Accuracy : %.4g" % metrics.accuracy_score(dtrain['Disbursed'].values, dtrain_predictions)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(dtrain['Disbursed'], dtrain_predprob)
                    
    feat_imp = pd.Series(alg.booster().get_fscore()).sort_values(ascending=False)
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')


# In[27]:

#Choose all predictors except target & IDcols
# predictors = [x for x in train.columns if x not in [target, IDcol]]
import xgboost as xgb
from xgboost.sklearn import XGBClassifier

xgb1 = XGBClassifier(
 learning_rate =0.1,
 n_estimators=1000,
 max_depth=5,
 min_child_weight=1,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 objective= 'binary:logistic',
 nthread=4,
 scale_pos_weight=1,
 seed=27)


# In[ ]:

modelfit(xgb1, x_train, y_train)


# In[30]:

import xgboost


# In[ ]:



