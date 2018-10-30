import numpy as np

import QueryGenerator as qg
import QueryClassifier as qc
import NeuralNetwork as nn

trainSet_dim = 0.7

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
    print len(dataSet), len(trainSet), len(testSet)
    print "TRAINSET:-----------------\n", trainSet
    print "TESTSET:-----------------\n", testSet
    return trainSet, testSet

# Read from files
legitStrings, maliciousStrings = qg.load_csvFiles()
# Create SQLI queries
legitSet, maliciousSet = qg.generate_dataset(legitStrings, maliciousStrings)
# Classify queries
classifiedLegits = qc.classify(legitSet)
classifiedMaliciouses = qc.classify(maliciousSet)
# Create train and test sets and labels for neural network
legitTrainSet, legitTestSet = splitSet(classifiedLegits)
legitTrainLabels = np.zeros((int)(trainSet_dim*len(classifiedLegits)), dtype=int)
maliciousTrainSet, maliciousTestSet = splitSet(classifiedMaliciouses)
maliciousTrainLabels = np.ones((int)(trainSet_dim*len(classifiedMaliciouses)), dtype=int)
# Merge two train sets and label sets
trainSet = np.append(legitTrainSet, maliciousTrainSet)
trainLabels = np.append(legitTrainLabels, maliciousTrainLabels)

neuralNetwork = nn.create_neural_network(qc.attack_keywords)
neuralNetwork.f
