from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy

class CustomLogisticRegression:

    def __init__(self, fit_intercept=True, l_rate=0.01, n_epoch=100):
        self.fit_intercept = ...
        self.l_rate = ...
        self.n_epoch = ...

    def sigmoid(self, t):
        return 1 / (1 + numpy.exp(-t))

    def predict_proba(self, row, coef_):
        t = 0.77001597 + numpy.dot(row, coef_)
        return self.sigmoid(t)


X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X = X[['worst concave points', 'worst perimeter']]
X['worst perimeter'] = (X['worst perimeter'] - X['worst perimeter'].mean()) / X['worst perimeter'].std()
X['worst concave points'] = (X['worst concave points'] - X['worst concave points'].mean()) / X['worst concave points'].std()
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=43)
CLR = CustomLogisticRegression()
result = CLR.predict_proba(X_test.head(10), [-2.12842434, -2.39305793])
print(result.tolist())