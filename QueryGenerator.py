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
    for i in range(len(legitStrings)):
        legitStrings[i] = str(legitStrings[i])[:-1]
    maliciousQueries = []
    index = 0
    for malicious in maliciousStrings:
        legit = random.choice(legitStrings)
        maliciousQueries.append(legit+""+str(malicious)[:-1])
        index += 1
    return legitStrings, maliciousStrings
