import numpy as np

import QueryClassifier as qc
import QueryGenerator as qg

trainSet_dim = 0.7

# Split set for train and test phases
def splitSet(dataSet):
    trainSet = np.zeros(((int)(trainSet_dim * len(dataSet)), len(qc.attack_keywords)),dtype=int)
    testSet = np.zeros((len(dataSet)-len(trainSet), len(qc.attack_keywords)), dtype=int)
    j = 0
    for i in range(len(dataSet)):
        if(i<(int)(trainSet_dim * len(dataSet))):
            trainSet[i] = dataSet[i]
        else:
            testSet[j] = dataSet[i]
            j += 1
    return trainSet, testSet

# Create datasets for neural network from csv files
def getDatasets():
    # Read from files
    legitStrings, maliciousStrings = qg.load_csvFiles()
    # Create SQL Injection queries
    legitSet, maliciousSet = qg.generate_dataset(legitStrings, maliciousStrings)
    # Classify queries
    classifiedLegits = qc.classify(legitSet)
    classifiedMaliciouses = qc.classify(maliciousSet)
    # Create train and test sets and labels for neural network
    legitTrainSet, legitTestSet = splitSet(classifiedLegits)
    legitTrainLabels = np.zeros((int)(trainSet_dim * len(classifiedLegits)), dtype=int)
    legitTestLabels = np.zeros((len(classifiedLegits) - len(legitTrainSet)), dtype=int)
    maliciousTrainSet, maliciousTestSet = splitSet(classifiedMaliciouses)
    maliciousTrainLabels = np.ones((int)(trainSet_dim * len(classifiedMaliciouses)), dtype=int)
    maliciousTestLabels = np.ones((len(classifiedMaliciouses) - len(maliciousTrainSet)), dtype=int)
    # Merge two train sets and label sets
    trainSet = np.vstack((legitTrainSet, maliciousTrainSet))
    trainLabels = np.append(legitTrainLabels, maliciousTrainLabels)
    testSet = np.vstack((legitTestSet, maliciousTestSet))
    testLabels = np.append(legitTestLabels, maliciousTestLabels)
    return trainSet, trainLabels, testSet, testLabels
