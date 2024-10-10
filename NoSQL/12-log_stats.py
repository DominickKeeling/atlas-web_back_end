#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip
The output of your script must be exactly the same as the example
"""
import pymongo
from pymongo import MongoClient


def log_stats():
  """Function to get stats about Nginx logs stored in MongoDB"""
  
  HOST = 'localhost'
  PORT = 27017
  DATABASE = 'logs'
  COLLECTION = 'nginx'
  
  """
  connects to mongodb
  """
  client = MongoClient(HOST, PORT)
  db = client[DATABASE]
  collection = db[COLLECTION]
  
  """ count the number of docss in collection"""
  total_docs = collection.count_documents({})
  print(f"{total_docs} logs")
  
  """counts methods"""
  methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
  method_counts = {method: collection.count_documents({"method": method}) for method in methods}
  
  """ print method count """
  for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
    
  """count status checks """
  status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
  print(f"{status_check_count} status check")
  

if __name__ == "__main__":
  log_stats()