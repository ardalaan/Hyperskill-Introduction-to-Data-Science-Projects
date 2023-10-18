import numpy as np
import pandas as pd
from sklearn import model_selection
import tensorflow as tf

(X_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_train[:6000], y_train[:6000], test_size=0.3, random_state=40)
print(f"""x_train shape: {X_train.shape}
x_test shape: {X_test.shape}
y_train shape: {y_train.shape}
y_test shape: {y_test.shape}
Proportion of samples per class in train set:
{pd.Series(y_train).value_counts(normalize=True)}""")