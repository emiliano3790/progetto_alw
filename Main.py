import numpy as np

import QueryClassifier as qc
import NeuralNetwork as nn
import Tools as tl

# Create train and test sets and labels
trainSet, trainLabels, testSet, testLabels = tl.getDatasets()
# Create neural network
neuralNetwork = nn.create_neural_network(len(qc.attack_keywords))
# Train neural network
neuralNetwork.fit(trainSet, trainLabels, epochs=75)
print neuralNetwork.summary()
# Test neural network
predictions = neuralNetwork.predict(testSet)
# Comparison between predictions and ground truth
j = 0
for k in range(len(predictions)):
    if np.argmax(predictions[k]) == testLabels[k]:
        j += 1
print j, len(predictions)
