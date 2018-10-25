import numpy as np

attack_keywords = ["CREATE TABLE","DELETE FROM","DROP TABLE","INSERT INTO","SELECT","UNION","UPDATE","SET","AND","OR",
                   "=","LIKE","load_file","information_schema","--","/*","*/"]#,"@@","sleep","DROP FUNCTION","WAITFOR",
                   #"ELT","exec","CTXSYS","CONVERT","CAST","UPPER","XMLType","UTL_INADDR","CREATE OR REPLACE FUNCTION",
                   #"DBMS_PIPE","DBMS_LOCK","NULL"]

def classify(queries):
    classificationSet = np.zeros((len(queries), len(attack_keywords)),dtype=int)
    for query_counter in range(len(queries)):
        query = queries[query_counter]
        for keyword_counter in range(len(attack_keywords)):
            keyword = attack_keywords[keyword_counter]
            if ((query.find(keyword) != -1) or (query.find(keyword.lower()) != -1) or (query.find(keyword.upper()) != -1)):
                classificationSet[query_counter][keyword_counter] = 1
    return classificationSet
