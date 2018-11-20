import numpy as np
from sklearn.metrics import confusion_matrix
import QueryClassifier as qc
import NeuralNetwork as nn
import Tools as tl

# Create balanced and unbalanced datasets to compare different neural networks
for balanceDatasets in range(0, 2):
    # Read data from files and create SQL injection queries
    legitSet, maliciousSet = tl.loadData(balanceDatasets)
    # Create output file
    workbook, sheet = tl.openOutputFile(balanceDatasets)
    # First row of output file
    row = 1
    # Vary number of features adding extra ones
    for setExtraFeatures in range(0, 2):
        # Varying number of attack keywordsfeatures, create and test different neural networks
        for featuresNum in qc.attackKeywordsSize:
            # Create train and test sets and labels
            trainSet, trainLabels, testSet, testLabels = tl.getDatasets(legitSet, maliciousSet, featuresNum, setExtraFeatures)
            # Create neural network
            if setExtraFeatures:
                neuralNetwork = nn.create_neural_network(featuresNum + 2)
            else:
                neuralNetwork = nn.create_neural_network(featuresNum)
            # Vary training process
            for epochsNum in range(10, 310, 10):
                # Train neural network
                neuralNetwork.fit(trainSet, trainLabels, epochsNum)
                print neuralNetwork.summary()
                # Test neural network
                predictions = neuralNetwork.predict(testSet)
                # Comparison between predictions and ground truth
                arg_max = np.zeros(len(predictions), dtype=int)
                for k in range(len(predictions)):
                    arg_max[k] = np.argmax(predictions[k])
                # Write confusion matrix on the output file
                cm = confusion_matrix(testLabels, arg_max)
                row = tl.writeResult(featuresNum, epochsNum, cm, sheet, row)
    tl.closeOutputFile(workbook)
