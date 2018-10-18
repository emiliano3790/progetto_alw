import csv
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
        maliciousQueries.append(legit+""+malicious)
        index += 1
    for i in range(0,10):
        print len(maliciousQueries[i]), maliciousQueries[i][60], maliciousQueries[i]

a, b = load_csvFiles()
generate_dataset(a, b)
