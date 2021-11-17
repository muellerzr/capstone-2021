from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from random import randint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client = MongoClient('mongodb+srv://Nick:BhKkB9LmdRMfA@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://Gabe:Pa55w0rd!@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db=client.credentials

serverStatusResult=db.command("serverStatus")
print(serverStatusResult)