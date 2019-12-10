#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import Bottle, route, run, request, abort
import pymongo
from pymongo import MongoClient
import datetime
import pprint

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# *** CRUD imported operations
def insert_document(document):
    try:
        result=collection.save(document)
    except:
        return False
    return True
  
def read_document(document):
    try:
        result = collection.find_one(document)
    except:
        return False
    return result
  
def read_documentProjection(document, projection):
    try:
        result = collection.find_one(document,projection)
    except:
        return False
    return result
  
def update_document(query, update):
    try:
        result = collection.update_one(query, update)
    except:
        return False
    return result
  
def delete_document(document):
    try:
        result = collection.delete_one(document)
    except:
        return False
    return result
# *** END CRUD imported operations
  
# set up URI paths for REST service

# delete /ticker
@route('/deleteStock/<ticker>', method = 'GET')
def delDoc(ticker):
    myDoc = {"Ticker" : ticker}
    string = delete_document(myDoc)


# create stockTicker
@route('/createStock/<ticker>', method='GET')
def createDoc(ticker):
    result = {"Ticker": ticker}
    insert_document(result)
    
  
# get stock/ticker
@route('/getStock/<ticker>', method='GET')
def findDoc(ticker):
    result = {"Ticker": ticker}
    result = read_document(result)
    if not result:
        abort(404, 'No Document found with id %s' % id)
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
    
  
# update /ticker /price
@route('/updateStock/<ticker>/<price>')
def updateDoc(ticker, price):
    myQuery = {"Ticker" : ticker}
    myUpdate = {"$set" : {"Price" : price}}
    result = update_document(myQuery, myUpdate)
    
# stockReport/list
@route('/stockReport/<list>', method='GET')
def stockReport(list):
    projection = {"Ticker" : 1, "Sector" : 1, "Industry" : 1, "Performance (YTD)" : 1, "Price" : 1, "50-Day Simple Moving Average": 1, "Shares Float": 1, "_id": 0}
    myDoc = {"Ticker": list}
    result = read_documentProjection(myDoc, projection)
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
  
# industryreport/industry
@route('/industryReport/<industry>')
def industryReport(industry):
    pipeline = ([
      {"$match": {"Industry" : industry}},
      {"$project" :{"Ticker": 1, "Profit Margin": 1, "_id": 0}},
      {"$sort" : {"Profit Margin" : -1}},
      {"$limit": 5}
    ])
    result = list(collection.aggregate(pipeline))
    string = json.dumps(result)
    return string
 
if __name__ == '__main__':
    #app.run(debug=True)
    run(host='localhost', port=8080)