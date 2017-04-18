from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler  
from sklearn import preprocessing
############################
##data pre processing
import pandas as pd 
import numpy as np 

train = pd.read_csv("~/scripts/balanced_train_joined.csv") #load dataframe train

train.fillna(0, inplace=True)

features = np.setdiff1d(list(train.columns),["Id","Response"]) #get the headers for feeature columns

# #replace nan with numbers in StartTime in train
# garbage = train.StartTime 

# gr = np.array(garbage)
# gr = np.nan_to_num(gr)
# train.StartTime = gr


X_train = np.array(train[features])

#normalizing data
normalizer = preprocessing.Normalizer().fit(X_train)
X_train = normalizer.transform(X_train)
Y_train = train.Response.ravel()

# Test data
test = pd.read_csv("/home/mma/MMA/FYP/Dataset/id-based-features-and-numeric-test.csv") #load test dataframe
test.fillna(0, inplace=True)

# #replace nan with numbers in StartTime in test
# garbage = test.StartTime 
# gr = np.array(garbage)
# gr = np.nan_to_num(gr)
# test.StartTime = gr

# get Ids for prediction file
IDS = test.Id

#testing samples
X_test = np.array(test[features])


#normalizing data
normalizer = preprocessing.Normalizer().fit(X_test)
X_test = normalizer.transform(X_test)

###########
## MLP model


scaler = StandardScaler() 

scaler.fit(X_train) 
X = scaler.transform(X_train)

#clf = MLPClassifier(activation='relu' ,solver='adam', alpha=0.01, hidden_layer_sizes=(97, 10, 2), random_state=1, 
#	shuffle=True,verbose=True,learning_rate='adaptive', max_iter=500, validation_fraction=.2)


clf = MLPClassifier(activation='relu' ,solver='adam', alpha=0.2, hidden_layer_sizes=(97, 10, 2), random_state=1, 
	shuffle=True,verbose=True,learning_rate='adaptive', max_iter=500, validation_fraction=.2)

print "MLP model training under parameters: \n \n " + str(clf)
Model = clf.fit(X_train, Y_train)



scaler.fit(X_test) 
X = scaler.transform(X_test)

predictions = clf.predict(X_test)

pred = pd.DataFrame({'Id': IDS,
						'Response': predictions})


pred = pred.set_index('Id')


pred.to_csv("pred_mlp.csv")
