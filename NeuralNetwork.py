import tensorflow as tf
from tensorflow import keras

def create_neural_network(inputDim):
    neurons = (int)(0.8 * inputDim)
    #print type(neurons)
    #print inputDim
    model = keras.Sequential([
        keras.layers.Dense(neurons, activation = tf.nn.relu, input_shape=(inputDim,)),
        keras.layers.Dense(neurons, activation=tf.nn.relu),
        keras.layers.Dense(2, activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    #print model.summary()
    return model




