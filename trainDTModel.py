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
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_absolute_error

import pickle

features=pd.read_csv('generated data/features.csv',header=None)
label=pd.read_csv('generated data/label.csv',header=None)

labels = np.array(label)
featureLst=features
features = np.array(features)

X_train,X_test,y_train,y_test=train_test_split(features,labels,random_state=42)

X_train = np.nan_to_num(X_train)
X_test = np.nan_to_num(X_test)

dt = DecisionTreeRegressor(max_depth=4) #best behave at 4, but would like the random value
dt.fit(X_train, y_train.ravel())

predictions = dt.predict(X_test)
errors = mean_absolute_error(y_test,predictions)
print('Mean Absolute Error:', errors, 'degrees.')

# Mean Absolute Error: 0.4916997157090445 degrees.

truth, = plt.plot(y_test, 'r')
prediction, = plt.plot(predictions, 'b')
plt.legend([truth, prediction], ["Truth", "Prediction"])
plt.title('Normal Decision Tree Regression')

plt.show()

filename = 'result/dtModel.sav'
pickle.dump(dt, open(filename, 'wb'))

# load the model from disk
loadModel = pickle.load(open(filename, 'rb'))
result = loadModel.score(X_test, y_test)
print(result)
#0.17552653254561612