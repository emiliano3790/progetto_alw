import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix
import QueryClassifier as qc
import NeuralNetwork as nn
import Tools as tl

# Create train and test sets and labels
trainSet, trainLabels, testSet, testLabels = tl.getDatasets()
# Create neural network
neuralNetwork = nn.create_neural_network(len(qc.attack_keywords))
# Train neural network
neuralNetwork.fit(trainSet, trainLabels, epochs=20)
print neuralNetwork.summary()
# Test neural network
predictions = neuralNetwork.predict(testSet)
# Comparison between predictions and ground truth
j = 0
arg_max = np.zeros(len(predictions), dtype=int)
for k in range(len(predictions)):
    arg_max[k] = np.argmax(predictions[k])
    if np.argmax(predictions[k]) == testLabels[k]:
        j += 1
cm = confusion_matrix(testLabels, arg_max)
print cm, cm[0][0]
print j, len(predictions)
#COmmento fittizio
