import numpy as np
import QueryGenerator as qg
import QueryClassifier as qc
#import NeuralNetwork as nn

legitStrings, maliciousStrings = qg.load_csvFiles()
legitSet, maliciousSet = qg.generate_dataset(legitStrings, maliciousStrings)

classifiedLegits = qc.classify(legitSet)
legitLabels = np.zeros(len(classifiedLegits), dtype=int)
classifiedMaliciouses = qc.classify(maliciousSet)
maliciousLabels = np.ones(len(classifiedMaliciouses), dtype=int)

for i in range(len(classifiedLegits)):
    print classifiedLegits[i], legitLabels[i]
print '\n\n'
for i in range(len(classifiedMaliciouses)):
    print classifiedMaliciouses[i], maliciousLabels[i]
