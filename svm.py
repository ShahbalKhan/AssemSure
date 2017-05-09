import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn import svm 

train = pd.read_csv("~/scripts/balanced_train_joined.csv") #load dataframe train
train.fillna(0, inplace=True)

feats = np.setdiff1d(list(train.columns), ['Id','Response'])

X_train = np.array(train[feats])
y_train = train.Response.ravel()


test = pd.read_csv("/home/mma/MMA/FYP/Dataset/id-based-features-and-numeric-test.csv")
IDS = test.Id

feats = np.setdiff1d(list(test.columns), ['Id'])

X_test = np.array(test[feats])

model = svm.SVC()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

pred = pd.DataFrame({'Id': IDS,
						'Response': y_pred})


pred = pred.set_index('Id')


pred.to_csv("pred_svm.csv")

