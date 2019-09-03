import sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')

print(data.head())
print(data.shape)
print(data.describe())

y = data.quality
x = data.drop('quality', axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.2,
                                                    random_state=123,
                                                    stratify=y)
# Normal Scaling
scaler = preprocessing.StandardScaler().fit(x_train)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Scaling with Transformer API
pipeline = make_pipeline(preprocessing.StandardScaler(),
                         RandomForestRegressor(n_estimators=100))

hyperparameters = {'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                   'randomforestregressor__max_depth' : [None, 5, 3, 1]}
clf = GridSearchCV(pipeline, hyperparameters, cv=10)

# Fit and tune model
clf.fit(x_train, y_train)

print(clf.best_params_)
print (clf.refit)
y_pred = clf.predict(x_test)

print(r2_score(y_test, y_pred))

print(mean_squared_error(y_test, y_pred))

# save model
joblib.dump(clf, 'rf_regressor.pkl')

# load model
'''
clf2 = joblib.load('rf_regressor.pkl')
'''