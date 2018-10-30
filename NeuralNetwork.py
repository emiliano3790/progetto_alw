import tensorflow as tf
from tensorflow import keras

def create_neural_network(input_dim):
    model = keras.Sequential([
        keras.layers.Dense(input_shape=(input_dim, )),
        keras.layers.Dense(13, activation=tf.nn.relu),
        keras.layers.Dense(2, activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model




