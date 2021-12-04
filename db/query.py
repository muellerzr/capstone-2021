from pymongo import MongoClient

client = MongoClient('mongodb+srv://<username>:<password>@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db=client.credentials
#fivestar = db.reviews.find_one({'rating': 5})
#print(fivestar)