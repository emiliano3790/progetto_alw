import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix
import QueryClassifier as qc
import NeuralNetwork as nn
import Tools as tl

# Read data from files and create SQL injection queries
legitSet, maliciousSet = tl.loadData()
# Create output file
workbook, sheet = tl.openOutputFile()
# First row of output file
row = 0
# Varying number of features, create and test different neural networks
for featuresNum in qc.featuresSizes:
    # Create train and test sets and labels
    trainSet, trainLabels, testSet, testLabels = tl.getDatasets(legitSet, maliciousSet, featuresNum)
    # Create neural network
    neuralNetwork = nn.create_neural_network(featuresNum)
    for epochsNum in range(10, 200, 10):
        # Train neural network
        neuralNetwork.fit(trainSet, trainLabels, epochsNum)
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
        row = tl.writeResult(featuresNum, epochsNum, cm, sheet, row)
        print cm, cm[0][0]
        print j, len(predictions)
        #Commento fittizio
tl.closeOutputFile(workbook)
