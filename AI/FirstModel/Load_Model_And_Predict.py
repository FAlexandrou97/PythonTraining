import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')

y = data.quality
x = data.drop('quality', axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.2,
                                                    random_state=123,
                                                    stratify=y)

clf2 = joblib.load('rf_regressor.pkl')
y_pred = clf2.predict(x_test)

print(r2_score(y_test, y_pred))

print(mean_squared_error(y_test, y_pred))

