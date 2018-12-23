import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
import QueryClassifier as qc
import NeuralNetwork as nn
import Tools as tl

# Variables
startEpochsNum = 10
endEpochsNum = 310
epochsGap = 10
k = 5     # Folds num
seed = 7  # Seed for random_state of StratifiedKFold

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
            # Create train and test sets and labels for test model
            trainSet, trainLabels, testSet, testLabels = tl.getDatasets(legitSet, maliciousSet, featuresNum,
                                                                        setExtraFeatures)
            # Create datasets for Cross Validation
            dataset, datasetLabels = tl.getDatasetsCV(legitSet, maliciousSet, featuresNum, setExtraFeatures)
            kfold = StratifiedKFold(n_splits=k, random_state=seed, shuffle=True)
            # Vary training process
            for epochsNum in range(startEpochsNum, endEpochsNum, epochsGap):

                ####### Test Model #######
                # Create neural network
                if setExtraFeatures:
                    neuralNetwork = nn.create_neural_network(featuresNum + 2)
                else:
                    neuralNetwork = nn.create_neural_network(featuresNum)
                # Train neural network
                neuralNetwork.fit(trainSet, trainLabels, epochsNum)
                print neuralNetwork.summary()
                # Test neural network
                predictions = neuralNetwork.predict(testSet)
                # Comparison between predictions and ground truth
                arg_max = np.zeros(len(predictions), dtype=int)
                for k in range(len(predictions)):
                    arg_max[k] = np.argmax(predictions[k])
                # Create confusion matrix
                cm = confusion_matrix(testLabels, arg_max)

                ####### Cross Validation #######
                # Create neural network
                if setExtraFeatures:
                    neuralNetwork = nn.create_neural_network(featuresNum + 2)
                else:
                    neuralNetwork = nn.create_neural_network(featuresNum)
                cvscores = []
                for trainSetCV, testSetCV in kfold.split(dataset, datasetLabels):
                    # Train neural network
                    neuralNetwork.fit(dataset[trainSetCV], datasetLabels[trainSetCV], epochsNum)
                    print neuralNetwork.summary()
                    # Evaluate the model accuracy
                    scores = neuralNetwork.evaluate(dataset[testSetCV], datasetLabels[testSetCV], verbose=0)
                    cvscores.append(scores[1] * 100)

                # Write results on the output file
                row = tl.writeResult(featuresNum, epochsNum, cm, np.mean(cvscores), np.std(cvscores), sheet, row)

    tl.closeOutputFile(workbook)
