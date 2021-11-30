from pymongo import MongoClient
from random import randint
username = "Gabe"
password = "Pa55w0rd!"
url = f'mongodb+srv://{username}:{password}@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.credentials

serverStatusResult=db.command("serverStatus")
print(serverStatusResult)