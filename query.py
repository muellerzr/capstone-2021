from pymongo import MongoClient

client = MongoClient('mongodb+srv://Nick:BhKkB9LmdRMfA@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db=client.business

fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)