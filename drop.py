from pymongo import MongoClient
client = MongoClient('mongodb+srv://Nick:BhKkB9LmdRMfA@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db=client.business

db.reviews.drop()