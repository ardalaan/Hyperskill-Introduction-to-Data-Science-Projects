import os
import requests

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error as mape

# checking ../Data directory presence
if not os.path.exists('../Data'):
    os.mkdir('../Data')

# download data if it is unavailable
if 'data.csv' not in os.listdir('../Data'):
    url = "https://www.dropbox.com/s/3cml50uv7zm46ly/data.csv?dl=1"
    r = requests.get(url, allow_redirects=True)
    open('../Data/data.csv', 'wb').write(r.content)

# read data
data = pd.read_csv('../Data/data.csv')

# write your code here
X = data.drop('salary', axis=1)
Y = data.salary
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
model = LinearRegression()
mape_values = []

X_train_no_rating = X_train.drop('rating', axis=1)
X_test_no_rating = X_test.drop('rating', axis=1)
model.fit(X_train_no_rating, y_train)
y_pred = model.predict(X_test_no_rating)
mape_values.append(mape(y_test, y_pred))

X_train_no_age = X_train.drop('age', axis=1)
X_test_no_age = X_test.drop('age', axis=1)
model.fit(X_train_no_age, y_train)
y_pred = model.predict(X_test_no_age)
mape_values.append(mape(y_test, y_pred))

X_train_no_experience = X_train.drop('experience', axis=1)
X_test_no_experience = X_test.drop('experience', axis=1)
model.fit(X_train_no_experience, y_train)
y_pred = model.predict(X_test_no_experience)
mape_values.append(mape(y_test, y_pred))

X_train_no_rating_age = X_train.drop(['rating', 'age'], axis=1)
X_test_no_rating_age = X_test.drop(['rating', 'age'], axis=1)
model.fit(X_train_no_rating_age, y_train)
y_pred = model.predict(X_test_no_rating_age)
mape_values.append(mape(y_test, y_pred))

X_train_no_rating_experience = X_train.drop(['rating', 'experience'], axis=1)
X_test_no_rating_experience = X_test.drop(['rating', 'experience'], axis=1)
model.fit(X_train_no_rating_experience, y_train)
y_pred = model.predict(X_test_no_rating_experience)
mape_values.append(mape(y_test, y_pred))

X_train_no_age_experience = X_train.drop(['age', 'experience'], axis=1)
X_test_no_age_experience = X_test.drop(['age', 'experience'], axis=1)
model.fit(X_train_no_age_experience, y_train)
y_pred = model.predict(X_test_no_age_experience)
mape_values.append(mape(y_test, y_pred))

print(round(min(mape_values), 5))