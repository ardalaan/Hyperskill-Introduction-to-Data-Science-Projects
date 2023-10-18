from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


class CustomLogisticRegression:

    def __init__(self, fit_intercept=True, l_rate=0.01, n_epoch=100):
        self.fit_intercept = fit_intercept
        self.l_rate = l_rate
        self.n_epoch = n_epoch
        self.mse_first_error = []
        self.mse_last_error = []
        self.log_loss_first_error = []
        self.log_loss_last_error = []

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
                if _ == 0:
                    self.mse_first_error.append(self.calc_error_mse(X_train, y_train))
                elif _ == self.n_epoch - 1:
                    self.mse_last_error.append(self.calc_error_mse(X_train, y_train))

    def fit_log_loss(self, X_train, y_train):
        # stochastic gradient descent implementation
        self.coef_ = np.zeros(4)

        for _ in range(self.n_epoch):
            for i, row in X_train.iterrows():
                y_hat = self.predict_proba(row, self.coef_)
                # update all weights
                self.coef_[0] = self.coef_[0] - ((self.l_rate * (y_hat - y_train[i])) / X_train.shape[0])
                for j in range(1, 4):
                    self.coef_[j] = self.coef_[j] - ((self.l_rate * (y_hat - y_train[i]) * row[j-1]) / X_train.shape[0])
                if _ == 0:
                    self.log_loss_first_error.append(self.calc_error_log_loss(X_train, y_train))
                elif _ == self.n_epoch - 1:
                    self.log_loss_last_error.append(self.calc_error_log_loss(X_train, y_train))

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

    def calc_error_mse(self, X_train, y_train):
        y_hat = []
        for i, row in X_train.iterrows():
            y_hat.append(self.predict_proba(row, self.coef_))
        y_hat = np.array(y_hat)
        return ((y_hat - y_train) ** 2).sum() / X_train.shape[0]

    def calc_error_log_loss(self, X_train, y_train):
        y_hat = []
        for i, row in X_train.iterrows():
            y_hat.append(self.predict_proba(row, self.coef_))
        y_hat = np.array(y_hat)
        return (y_train * np.log10(y_hat) + (1 - y_train) * np.log10(1 - y_hat)).sum() / -X_train.shape[0]


X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X = X[['worst concave points', 'worst perimeter', 'worst radius']]
X = (X - X.mean()) / X.std()
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=43)

lr_mse = CustomLogisticRegression(fit_intercept=True, l_rate=0.01, n_epoch=1000)
lr_log_loss = CustomLogisticRegression(fit_intercept=True, l_rate=0.01, n_epoch=1000)
lr_sk = LogisticRegression()

lr_mse.fit_mse(X_train, y_train)
lr_log_loss.fit_log_loss(X_train, y_train)
lr_sk.fit(X_train, y_train)

predictions_mse = lr_mse.predict(X_test)
predictions_log_los = lr_log_loss.predict(X_test)
predictions_sk = lr_sk.predict(X_test)
print({'mse_accuracy': accuracy_score(y_test, predictions_mse), 'logloss_accuracy': accuracy_score(y_test, predictions_log_los), 'sklearn_accuracy': accuracy_score(y_test, predictions_sk), 'mse_error_first': lr_mse.mse_first_error, 'mse_error_last': lr_mse.mse_last_error, 'logloss_error_first': lr_log_loss.log_loss_first_error, 'logloss_error_last': lr_log_loss.log_loss_last_error})
print("""Answers to the questions:
1) 0.00000
2) 0.00000
3) 0.00152
4) 0.00600
5) expanded
6) expanded""")
# print({'coef_': lr.coef_.tolist(), 'accuracy': accuracy_score(y_test, predictions)})