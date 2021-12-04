from pymongo import MongoClient

username = "" #mongo username
password = "" #mongo password
url = f'mongodb+srv://{username}:{password}@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=True&w=majority'
client = MongoClient(url)
db = client.credentials


serverStatusResult=db.command("serverStatus")
print(serverStatusResult)