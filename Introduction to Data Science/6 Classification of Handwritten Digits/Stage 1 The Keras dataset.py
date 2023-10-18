import numpy as np
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(60000, 784)
print(f"""Classes: {np.unique(y_train)}
Feature's shape: {X_train.shape}
Target's shape: {y_train.shape}
min: {X_train.min()}, max: {X_train.max()}""")