import random

# Open csv files with legit SQL queries and malicious attack strings
def load_csvFiles():
    # Load data of legit queries
    with open('Dataset/legit.csv', mode='r') as legitFile:
        legitStrings = list(legitFile)
    # Load data of SQL injection attacks
    with open('Dataset/malicious.csv', mode='r') as maliciousFile:
        maliciousStrings = list(maliciousFile)
    return legitStrings, maliciousStrings


# Create malicious SQL queries concatenating a legit query with an attack string
def generate_dataset(legitStrings, maliciousStrings):
    for i in range(len(legitStrings)):
        # Remove '\n' at the end of the string
        legitStrings[i] = str(legitStrings[i])[:-1]
    maliciousQueries = []
    index = 0
    for malicious in maliciousStrings:
        # Select random legit query
        legit = random.choice(legitStrings)
        # Concatenate query and malicious string (removing '\n' at the end)
        maliciousQueries.append(legit+""+str(malicious)[:-1])
        index += 1
    # Mix lists
    random.shuffle(legitStrings)
    random.shuffle(maliciousStrings)
    return legitStrings, maliciousStrings
