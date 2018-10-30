import tensorflow as tf
from tensorflow import keras

# Create a neural network with the given size of the input layer
def create_neural_network(inputDim):
    hiddenLayer_neurons = (int)(0.8 * inputDim)     # Num of neurons in the hidden layer
    model = keras.Sequential([
        keras.layers.Dense(hiddenLayer_neurons, activation = tf.nn.relu, input_shape=(inputDim,)),  # 1st hidden layer
        keras.layers.Dense(hiddenLayer_neurons, activation=tf.nn.relu),                             # 2nd hidden layer
        keras.layers.Dense(2, activation=tf.nn.softmax)                                             # Output layer
    ])
    model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model




