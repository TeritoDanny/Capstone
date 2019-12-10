import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# basic function for inserting a new document
def insert_document(document):
    try:
        result=collection.save(document)
    except:
        return False
    return True
  
# basic function to retrieve a single document
def read_document(document):
    try:
        result = collection.find_one(document)
    except:
        return False
    return result

# basic function for updating a document  
def update_document(query, update):
    try:
        result = collection.update_one(query, update)
    except:
        return False
    return result

# basic function to delete a document  
def delete_document(document):
    try:
        result = collection.delete_one(document)
    except:
        return False
    return result
  
def main():
    print
    print "INSERT"
    print "Now lets submit a key-value pair of Ticker:DNZ and Return on Investment:0175"
    myDocument = { "Ticker" : "DNZ", "Return on Investment" : 0.175}
    print insert_document(myDocument)
    print "Verify that we inserted that document"
    myDocument = {"Ticker" : "DNZ"}
    print read_document(myDocument)
    print
    print "UPDATE"
    print "Let's update our DNZ ticker"
    myQuery = {"Ticker" : "DNZ"}
    myDocument = {"$set" : {"Company" : "DNZ Programming"}}
    print update_document(myQuery, myDocument)
    print read_document(myQuery)
    print 
    print "DELETE"
    print "Now we will delete the just updated one above"
    myDocument = {"Ticker" : "DNZ"}
    print delete_document(myDocument)
    print "See if we can find the Ticker DNZ:"
    print read_document(myQuery)
    print
    
main()
