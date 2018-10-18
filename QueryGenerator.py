import csv
import random

def load_csvFiles():
    # Load data of legit queries
    with open('Dataset/legit.csv', mode='r') as legitFile:
        legitStrings = csv.reader(legitFile)
    # Load data of SQL injection attacks
    with open('Dataset/malicious.csv', mode='r') as maliciousFile:
        maliciousStrings = csv.reader(maliciousFile)
    return legitStrings, maliciousStrings

def generate_dataset(legitStrings, maliciousStrings):
    for malicious in maliciousStrings:
        legit = random.choice(legitStrings)
        maliciousString = legit + malicious
        print maliciousString
