import xlsxwriter
import numpy as np
import math

import QueryClassifier as qc
import QueryGenerator as qg

trainSet_dim = 0.7

def openOutputFile():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Results.xlsx')
    sheet = workbook.add_worksheet()
    # Write header line
    sheet.write(0, 0, 'featuresNum')
    sheet.write(0, 1, 'epochsNum')
    sheet.write(0, 2, 'TN')
    sheet.write(0, 3, 'FP')
    sheet.write(0, 4, 'FN')
    sheet.write(0, 5, 'TP')
    return workbook, sheet

def writeResult(featuresNum, epochsNum, confusion_matrix, sheet, row):
    # Write data
    sheet.write(row, 0, featuresNum)
    sheet.write(row, 1, epochsNum)
    col = 2
    for elem in confusion_matrix:
        sheet.write(row, col, elem[0])
        sheet.write(row, col + 1, elem[1])
        col += 2
    return row+1

def closeOutputFile(workbook):
    workbook.close()

def loadData():
    # Read from files
    legitStrings, maliciousStrings = qg.load_csvFiles()
    # Create SQL Injection queries
    legitSet, maliciousSet = qg.generate_dataset(legitStrings, maliciousStrings)
    return legitSet, maliciousSet

# Split set for train and test phases
def splitSet(dataSet, featuresNum, setExtraFeatures):
    if setExtraFeatures:
        trainSet = np.zeros(((int)(trainSet_dim * len(dataSet)), featuresNum + 2), dtype=float)
        testSet = np.zeros((len(dataSet) - len(trainSet), featuresNum + 2), dtype=float)
    else:
        trainSet = np.zeros(((int)(trainSet_dim * len(dataSet)), featuresNum), dtype=float)
        testSet = np.zeros((len(dataSet) - len(trainSet), featuresNum), dtype=float)
    j = 0
    for i in range(len(dataSet)):
        if(i<(int)(trainSet_dim * len(dataSet))):
            trainSet[i] = dataSet[i]
        else:
            testSet[j] = dataSet[i]
            j += 1
    return trainSet, testSet

# Create datasets for neural network from csv files
def getDatasets(legitSet, maliciousSet, featuresNum, setExtraFeatures):
    # Classify queries
    classifiedLegits = qc.classify(legitSet, featuresNum, setExtraFeatures)
    classifiedMaliciouses = qc.classify(maliciousSet, featuresNum, setExtraFeatures)
    # Create train and test sets and labels for neural network
    legitTrainSet, legitTestSet = splitSet(classifiedLegits, featuresNum, setExtraFeatures)
    legitTrainLabels = np.zeros((int)(trainSet_dim * len(classifiedLegits)), dtype=float)
    legitTestLabels = np.zeros((len(classifiedLegits) - len(legitTrainSet)), dtype=float)
    maliciousTrainSet, maliciousTestSet = splitSet(classifiedMaliciouses, featuresNum, setExtraFeatures)
    maliciousTrainLabels = np.ones((int)(trainSet_dim * len(classifiedMaliciouses)), dtype=float)
    maliciousTestLabels = np.ones((len(classifiedMaliciouses) - len(maliciousTrainSet)), dtype=float)
    # Merge two train sets and label sets
    trainSet = np.vstack((legitTrainSet, maliciousTrainSet))
    trainLabels = np.append(legitTrainLabels, maliciousTrainLabels)
    testSet = np.vstack((legitTestSet, maliciousTestSet))
    testLabels = np.append(legitTestLabels, maliciousTestLabels)
    return trainSet, trainLabels, testSet, testLabels

# Compute Shannon entropy of the given string (query)
def shannonEntropy(string):
    # Count occurences of characters
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    # Compute entropy
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy