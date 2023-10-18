from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
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
    return score


(X_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_train, X_test, y_train, y_test = train_test_split(X_train[:6000], y_train[:6000], test_size=0.3, random_state=40)

normalizer = Normalizer().fit(X_train)
X_train_norm = normalizer.transform(X_train)
X_test_norm = normalizer.transform(X_test)

KNN_param = {'n_neighbors': [3, 4], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'brute']}
RF_param = {'n_estimators': [300, 500], 'max_features': ['sqrt', 'log2'], 'class_weight':
    ['balanced', 'balanced_subsample']}

KNN_grid_search = GridSearchCV(estimator=KNeighborsClassifier(), param_grid=KNN_param, scoring='accuracy', n_jobs=-1)
RF_grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=40), param_grid=RF_param, scoring='accuracy', n_jobs=-1)

KNN_grid_search.fit(X_train_norm, y_train)
RF_grid_search.fit(X_train_norm, y_train)

KNN_best_estimator = KNN_grid_search.best_estimator_
RF_best_estimator = RF_grid_search.best_estimator_

print(f"""K-nearest neighbours algorithm
best estimator: {KNN_best_estimator}
accuracy: {fit_predict_eval(
        model=KNN_best_estimator,
        features_train=X_train_norm,
        features_test=X_test_norm,
        target_train=y_train,
        target_test=y_test
    )}

Random forest algorithm
best estimator: {RF_best_estimator}
accuracy: {fit_predict_eval(
        model=RF_best_estimator,
        features_train=X_train_norm,
        features_test=X_test_norm,
        target_train=y_train,
        target_test=y_test
    )}""")