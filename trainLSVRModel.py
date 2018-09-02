import module_manager
module_manager.review()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import seaborn as sns

from sklearn import decomposition
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import utils
from sklearn import svm
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

#linear svr
linearM2=svm.LinearSVR().fit(X_train,y_train.ravel())

predictionsLM2 = linearM2.predict(X_test)
errors = mean_absolute_error(y_test,predictionsLM2)
print('Mean Absolute Error for LM2:', errors, 'degrees.')

# Mean Absolute Error for LM2: 0.5539626512183776 degrees.

truth, = plt.plot(y_test, 'r',label='Truth')
prediction, = plt.plot(predictionsLM2, 'b',label='Prediction')
plt.legend()
plt.title('Linear Support Vector Regressor')

plt.show()

filename = 'result/lsvm2Model.sav'
pickle.dump(linearM2, open(filename, 'wb'))

# load the model from disk
loadModel = pickle.load(open(filename, 'rb'))
result = loadModel.score(X_test, y_test)
print(result)
#-0.08088613659947197