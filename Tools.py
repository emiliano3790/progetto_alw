import xlswriter
import numpy as np

import QueryClassifier as qc
import QueryGenerator as qg

trainSet_dim = 0.7

def openOutputFile():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Results.xlsx')
    sheet = workbook.add_worksheet()
    return workbook, sheet

def writeResult(featuresNum, epochsNum, confusion_matrix, sheet, row):
    # Write data
    sheet.write(row, 0, featuresNum)
    sheet.write(row, 1, epochsNum)
    col = 2
    for elem in confusion_matrix:
        sheet.write(row, col, elem)
        col += 1
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
def splitSet(dataSet, featuresNum):
    trainSet = np.zeros(((int)(trainSet_dim * len(dataSet)), featuresNum), dtype=int)
    testSet = np.zeros((len(dataSet) - len(trainSet), featuresNum), dtype=int)
    j = 0
    for i in range(len(dataSet)):
        if(i<(int)(trainSet_dim * len(dataSet))):
            trainSet[i] = dataSet[i]
        else:
            testSet[j] = dataSet[i]
            j += 1
    return trainSet, testSet

# Create datasets for neural network from csv files
def getDatasets(legitSet, maliciousSet, featuresNum):
    # Classify queries
    classifiedLegits = qc.classify(legitSet, featuresNum)
    classifiedMaliciouses = qc.classify(maliciousSet, featuresNum)
    # Create train and test sets and labels for neural network
    legitTrainSet, legitTestSet = splitSet(classifiedLegits, featuresNum)
    legitTrainLabels = np.zeros((int)(trainSet_dim * len(classifiedLegits)), dtype=int)
    legitTestLabels = np.zeros((len(classifiedLegits) - len(legitTrainSet)), dtype=int)
    maliciousTrainSet, maliciousTestSet = splitSet(classifiedMaliciouses, featuresNum)
    maliciousTrainLabels = np.ones((int)(trainSet_dim * len(classifiedMaliciouses)), dtype=int)
    maliciousTestLabels = np.ones((len(classifiedMaliciouses) - len(maliciousTrainSet)), dtype=int)
    # Merge two train sets and label sets
    trainSet = np.vstack((legitTrainSet, maliciousTrainSet))
    trainLabels = np.append(legitTrainLabels, maliciousTrainLabels)
    testSet = np.vstack((legitTestSet, maliciousTestSet))
    testLabels = np.append(legitTestLabels, maliciousTestLabels)
    return trainSet, trainLabels, testSet, testLabels
