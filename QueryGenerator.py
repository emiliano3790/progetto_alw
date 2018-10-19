import random
import numpy as np

def load_csvFiles():
    # Load data of legit queries
    with open('Dataset/legit.csv', mode='r') as legitFile:
        legitStrings = list(legitFile)
    # Load data of SQL injection attacks
    with open('Dataset/malicious.csv', mode='r') as maliciousFile:
        maliciousStrings = list(maliciousFile)
    return legitStrings, maliciousStrings

def generate_dataset(legitStrings, maliciousStrings):
    maliciousQueries = []
    index = 0
    for malicious in maliciousStrings:
        legit = random.choice(legitStrings)
        maliciousQueries.append(str(legit)[:-1]+""+str(malicious)[:-1])
        index += 1
    # for i in range(0,10):
    #     print len(maliciousQueries[i]), maliciousQueries[i][60], maliciousQueries[i]
    # DA PROVARE
    legitSet = np.array((legit,2))
    for i in range(legitSet.shape[0]):
        legitSet[i][1] = 0
    maliciousSet = np.array((maliciousQueries, 2))
    for i in range(maliciousSet.shape[0]):
        maliciousSet[i][1] = 1
    queryDataSet = legitSet
    queryDataSet.append(maliciousSet)
    queryDataSet.shuffle()

a, b = load_csvFiles()
generate_dataset(a, b)
