from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf


def fit_predict_eval(model, features_train, features_test, target_train, target_test):
    # here you fit the model
    model.fit(features_train, target_train)
    # make a prediction
    predictions = model.predict(features_test)
    # calculate accuracy and save it to score
    score = accuracy_score(target_test, predictions)
    print(f'Model: {model}\nAccuracy: {score}\n')


(X_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_train, X_test, y_train, y_test = train_test_split(X_train[:6000], y_train[:6000], test_size=0.3, random_state=40)

fit_predict_eval(
        model=KNeighborsClassifier(),
        features_train=X_train,
        features_test=X_test,
        target_train=y_train,
        target_test=y_test
    )
fit_predict_eval(
        model=DecisionTreeClassifier(random_state=40),
        features_train=X_train,
        features_test=X_test,
        target_train=y_train,
        target_test=y_test
    )
fit_predict_eval(
        model=LogisticRegression(random_state=40),
        features_train=X_train,
        features_test=X_test,
        target_train=y_train,
        target_test=y_test
    )
fit_predict_eval(
        model=RandomForestClassifier(random_state=40),
        features_train=X_train,
        features_test=X_test,
        target_train=y_train,
        target_test=y_test
    )
print("The answer to the question: RandomForestClassifier - 0.939")