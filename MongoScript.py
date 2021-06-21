import pymongo, sys
import json
import pandas as pd

def correct_encoding(dictionary):
    """Correct the encoding of python dictionaries so they can be encoded to mongodb
    inputs
    -------
    dictionary : dictionary instance to add as document
    output
    -------
    new : new dictionary with (hopefully) corrected encodings"""
    import numpy as np
    new = {}
    for key1, val1 in dictionary.items():
        # Nested dictionaries
        if isinstance(val1, dict):
            val1 = correct_encoding(val1)

        if isinstance(val1, np.bool_):
            val1 = bool(val1)

        if isinstance(val1, np.int64):
            val1 = int(val1)

        if isinstance(val1, np.float64):
            val1 = float(val1)

        new[key1] = val1

    return new

client = pymongo.MongoClient("localhost", 27017)
print(client.list_database_names())
db_list = client.list_database_names()

for i in range(len(db_list)):
    print("{})".format(i), db_list[i])

try:
    selected_db = int(input("which database you want in? "))
except ValueError:
    print("selected index should be an integer, try again. ")
    selected_db = int(input("which database you want in? "))

# Example of Creating a database or access to the database did not exist unless you create sthg in the database
db = client[db_list[selected_db]]
print(f"Now you are in database named: {db.name}")

# Listing collections within the database
col_list = db.list_collection_names()
for i in range(len(col_list)):
    print("{})".format(i), col_list[i])

try:
    selected_col = int(input("which collection you want in? "))
except ValueError:
    print("selected index should be an integer, try again. ")
    selected_col = int(input("which collection you want in? "))

collection = db[col_list[selected_col]]
print(f"Now you are in collection named: {collection.name}")
print(f"The docs in this collection: {collection.estimated_document_count()}")

# inserting files from csv
df = pd.read_csv("file_path")
new = {}
doc_list = []

for i in range(len(df)):    
    for key in col_list:
        new[key] = df[key][i]
        doc_list.append(new)
        new = {}

new_doc_list = []
for doc in doc_list:
    new_doc = correct_encoding(doc)
    new_doc_list.append(new_doc)

collection.insert_many(new_doc_list)


"""
Docs template 
{   
    "Code_Name" : str
    "Name" : str
    "Patient_ID" : series of number (str?)
    "Age" : int
    "Gender" : Numeric 0 for male, 1 for female, 3 for unspoken
    "Images" : {
        "mfalff" : Array
        "mreho" : Array
        "iso" : Array
        "gfa" : Array
        "nqa" : Array
    }

    "Psychological_Questionaire" : {
        "HAMD" : Numeric
        "PhQ" : Numeric
        etc...
    }

}
"""
