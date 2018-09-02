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
from sklearn.linear_model import LinearRegression
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

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
errors = mean_absolute_error(y_test,predictions)
print('Mean Absolute Error:', errors, 'degrees.')

# Mean Absolute Error: 0.46421857152619195 degrees.

truth, = plt.plot(y_test, 'r')
prediction, = plt.plot(predictions, 'b')
plt.legend([truth, prediction], ["Truth", "Prediction"])
plt.title('Linear Regression')

plt.show()

filename = 'result/lrModel.sav'
pickle.dump(model, open(filename, 'wb'))

# load the model from disk
loadModel = pickle.load(open(filename, 'rb'))
result = loadModel.score(X_test, y_test)
print(result)
#0.2658618344139453