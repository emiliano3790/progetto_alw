import numpy as np

# List of SQL injection attack keywords
attack_keywords = ["CREATE TABLE","DELETE FROM","DROP TABLE","INSERT INTO","SELECT","UNION","UPDATE","SET","AND","OR",
                   "=","LIKE","load_file","information_schema","--","/*","*/"]#,"@@","sleep","DROP FUNCTION","WAITFOR",
                   #"ELT","exec","CTXSYS","CONVERT","CAST","UPPER","XMLType","UTL_INADDR","CREATE OR REPLACE FUNCTION",
                   #"DBMS_PIPE","DBMS_LOCK","NULL"]

# Convert a query into a features binary vector
def classify(queries):
    # Fill vector with zeros
    classificationSet = np.zeros((len(queries), len(attack_keywords)),dtype=int)
    for query_counter in range(len(queries)):
        # Select a query from the list
        query = queries[query_counter]
        for keyword_counter in range(len(attack_keywords)):
            # Select a keyword (feature) from the list
            keyword = attack_keywords[keyword_counter]
            # Check if query contains the selected keyword
            if((query.find(keyword) != -1) or (query.find(keyword.lower()) != -1) or (query.find(keyword.upper()) != -1)):
                # Set vector element as 1
                classificationSet[query_counter][keyword_counter] = 1
    return classificationSet
