import numpy as np
import random

import sys

import QueryGenerator as qg
import QueryClassifier as qc
#import NeuralNetwork as nn

trainSet_dim = 0.7
testSet_dim = 0.3

def splitSet(dataSet):
    trainSet = np.zeros(((int)(trainSet_dim * len(dataSet)), len(qc.attack_keywords)),dtype=int)
    testSet = np.zeros(((int)(testSet_dim * len(dataSet)), len(qc.attack_keywords)), dtype=int)
    j = 0
    for i in range(len(dataSet)):
        if(i<(int)(trainSet_dim * len(dataSet))):
            trainSet[i] = dataSet[i]
        else:
            testSet[j] = dataSet[i]
            j += 1
    print dataSet.shape, trainSet.shape, testSet.shape
    print "TRAINSET:-----------------\n", trainSet
    print "TESTSET:-----------------\n", testSet

legitStrings, maliciousStrings = qg.load_csvFiles()
legitSet, maliciousSet = qg.generate_dataset(legitStrings, maliciousStrings)

classifiedLegits = qc.classify(legitSet)
legitLabels = np.zeros(len(classifiedLegits), dtype=int)
classifiedMaliciouses = qc.classify(maliciousSet)
maliciousLabels = np.ones(len(classifiedMaliciouses), dtype=int)

splitSet(classifiedLegits)
