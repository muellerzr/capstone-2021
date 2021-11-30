from pymongo import MongoClient
username = "Gabe"
password = "Pa55w0rd!"
url = f'mongodb+srv://{username}:{password}@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority'
client = MongoClient(url)
# db = client.business
db = client.credentials

db.credentials.drop()