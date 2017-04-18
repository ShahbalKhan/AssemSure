from xgboost import XGBClassifier 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

train = pd.read_csv("/home/mma/MMA/FYP/Dataset/id-based-features-train.csv") #load dataframe train
train.fillna(-9999, inplace=True)

feats = np.setdiff1d(list(train.columns), ['Id','Response'])

x = np.array(train[feats])
y = train.Response.ravel()

seed = 7
test_size = 0.33

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)



model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Acc : %.2f%%" % (accuracy * 100.0))

