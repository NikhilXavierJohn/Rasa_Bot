import csv
import json
from pymongo import MongoClient

csvfile = open('hotels.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient('localhost', 27017) 
db=mongo_client['Hotels']
db.data.drop()
header= ["ApplicationNumber","ApprovalNumber","HotelName","Address","City","State","NodalOfficerName","MobileNumber","PhoneNumber","Email","Website","Category","SubCategory","TotalRooms","StartDate","ExpiryDate"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.data.insert(row)