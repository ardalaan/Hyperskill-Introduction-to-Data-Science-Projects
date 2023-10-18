from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


class CustomLogisticRegression:

    def __init__(self, fit_intercept=True, l_rate=0.01, n_epoch=100):
        self.fit_intercept = fit_intercept
        self.l_rate = l_rate
        self.n_epoch = n_epoch

    def sigmoid(self, t):
        return 1 / (1 + np.exp(-t))

    def predict_proba(self, row, coef_):
        t = coef_[0] + np.dot(row, coef_[1:])
        return self.sigmoid(t)

    def fit_mse(self, X_train, y_train):
        self.coef_ = np.zeros(4)

        for _ in range(self.n_epoch):
            for i, row in X_train.iterrows():
                y_hat = self.predict_proba(row, self.coef_)
                # update all weights
                self.coef_[0] = self.coef_[0] - (self.l_rate * (y_hat - y_train[i]) * y_hat * (1 - y_hat))
                for j in range(1, 4):
                    self.coef_[j] = self.coef_[j] - (
                                self.l_rate * (y_hat - y_train[i]) * y_hat * (1 - y_hat) * row[j-1])

    def predict(self, X_test, cut_off=0.5):
        predictions = []
        for i, row in X_test.iterrows():
            y_hat = self.predict_proba(row, self.coef_)
            if y_hat < cut_off:
                y_hat = 0
            else:
                y_hat = 1
            predictions.append(y_hat)
        return predictions  # predictions are binary values - 0 or 1


X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X = X[['worst concave points', 'worst perimeter', 'worst radius']]
X = (X - X.mean()) / X.std()
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=43)
lr = CustomLogisticRegression(fit_intercept=True, l_rate=0.01, n_epoch=1000)
lr.fit_mse(X_train, y_train)
predictions = lr.predict(X_test)
print({'coef_': lr.coef_.tolist(), 'accuracy': accuracy_score(y_test, predictions)})