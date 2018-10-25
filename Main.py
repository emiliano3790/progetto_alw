import numpy as np
import random

import sys

import QueryGenerator as qg
import QueryClassifier as qc
#import NeuralNetwork as nn

trainSet_dim = 0.7
testSet_dim = 0.3

legitStrings, maliciousStrings = qg.load_csvFiles()
legitSet, maliciousSet = qg.generate_dataset(legitStrings, maliciousStrings)

classifiedLegits = qc.classify(legitSet)
legitLabels = np.zeros(len(classifiedLegits), dtype=int)
classifiedMaliciouses = qc.classify(maliciousSet)
maliciousLabels = np.ones(len(classifiedMaliciouses), dtype=int)

# for i in range(len(classifiedLegits)):
#     print classifiedLegits[i], legitLabels[i]
# print '\n\n'
# for i in range(len(classifiedMaliciouses)):
#     print classifiedMaliciouses[i], maliciousLabels[i]

np.set_printoptions(threshold=sys.maxint)
print classifiedLegits, '\n\n'
np.random.shuffle(classifiedLegits)
#print classifiedLegits
legit_trainSet = np.array((trainSet_dim*len(classifiedLegits),len(qc.attack_keywords)),dtype=int)
for i in range((int)(trainSet_dim*len(classifiedLegits))):
    s = random.choice(classifiedLegits)
    np.append(legit_trainSet, random.choice(classifiedLegits))
len(qc.attack_keywords)
