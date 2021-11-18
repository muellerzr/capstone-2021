from pymongo import MongoClient
# client = MongoClient('mongodb+srv://Nick:BhKkB9LmdRMfA@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://Gabe:Pa55w0rd!@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.business
db = client.credentials

db.credentials.drop()