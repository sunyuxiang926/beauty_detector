import module_manager
module_manager.review()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import decomposition
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error

import pickle

features=pd.read_csv('generated data/features.csv',header=None)
label=pd.read_csv('generated data/label.csv',header=None)

labels = np.array(label)
featureLst=features
features = np.array(features)

X_train,X_test,y_train,y_test=train_test_split(features,labels,random_state = 42)

X_train = np.nan_to_num(X_train)
X_test = np.nan_to_num(X_test)

rf = RandomForestRegressor(n_estimators = 250, random_state = 42)
rf.fit(X_train, y_train.ravel())

predictions = rf.predict(X_test)
errors = mean_absolute_error(y_test,predictions)
print('Mean Absolute Error:', errors, 'degrees.')

# Training Features Shape: (3896, 17)
# Training Labels Shape: (3896, 1)
# Testing Features Shape: (1299, 17)
# Testing Labels Shape: (1299, 1)
# Mean Absolute Error: 0.4595141354161076 degrees.

truth, = plt.plot(y_test, 'r')
prediction, = plt.plot(predictions, 'b')
plt.legend([truth, prediction], ["Truth", "Prediction"])
plt.title('Random Forest Regression')

plt.show()

filename = 'result/rfModel.sav'
pickle.dump(rf, open(filename, 'wb'))

# load the model from disk
loadModel = pickle.load(open(filename, 'rb'))
result = loadModel.score(X_test, y_test)
print(result)
#0.2666280750504987