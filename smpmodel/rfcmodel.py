# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 06:31:13 2022

@author: Jae Lee
"""

# In[1]:

## Pre-import
import numpy as np
import pandas as pd
import warnings

import pickle

warnings.filterwarnings("ignore")

dataset = pd.read_excel('smpdata.xlsx')
data = dataset.iloc[ : ,1:9].values
target = dataset.iloc[ : ,11].values


from sklearn.model_selection import train_test_split
Xtrain_o, Xtest_o, Ytrain, Ytest = train_test_split(data,target,test_size=0.2)
test_number = np.array(Ytest.shape)

from sklearn.preprocessing import MinMaxScaler


# Instantiation
scaler = MinMaxScaler()  
Xtrain = scaler.fit_transform(Xtrain_o)  
Xtest = scaler.transform(Xtest_o)  


## Random Forest Regressor
# Determination of n_estimators
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
Vtr = []
tr = []
te = []
for i in range(20):
    rfr = RandomForestRegressor(criterion="mse"
                                ,random_state=0
                                ,n_estimators=10*i+1
                                ,max_depth=8)
    rfr = rfr.fit(Xtrain, Ytrain)
    rfr_s = cross_val_score(rfr,Xtrain,Ytrain,cv=10).mean()
    score_tr = rfr.score(Xtrain,Ytrain)
    score_te = rfr.score(Xtest,Ytest)
    Vtr.append(rfr_s)
    tr.append(score_tr)
    te.append(score_te)


# In[11]:

# Optimised model
# from sklearn.ensemble import RandomForestRegressor
rfc = RandomForestRegressor(criterion="mse"
                                ,random_state=0
                                ,n_estimators=102
                                ,max_depth=8)
rfc = rfc.fit(Xtrain, Ytrain)
rfc_score = cross_val_score(rfc,Xtrain,Ytrain,cv=10)
rfc_s = cross_val_score(rfc,Xtrain,Ytrain,cv=10).mean()
Ytrain_RF = rfc.predict(Xtrain)
Ytest_RF = rfc.predict(Xtest)

rfc_model=rfc.fit(Xtrain,Ytrain)

pickle.dump(rfc_model,open('rfc_model.pkl','wb'))



