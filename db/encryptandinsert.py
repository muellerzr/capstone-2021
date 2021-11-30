import sys, bcrypt
from pymongo import MongoClient

# https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python

def getHashedPassphrase(passphrase):
    encodedPassphrase = str.encode(passphrase)
    salt = bcrypt.gensalt()
    # print("salt = " + salt.decode("utf-8"))     #-----dbg!!!
    # print(salt)     #-----dbg!!!
    return str(bcrypt.hashpw(encodedPassphrase, salt))

def insertIntoDatabase(username, hashed_passphrase):
    username = "Gabe"
    password = "Pa55w0rd!"
    url = f'mongodb+srv://{username}:{password}@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority'
    client = MongoClient(url)
    
    db = client.credentials
    credential = {
        'username' : username,
        'passphrase' : hashed_passphrase
    }
    result = db.credentials.insert_one(credential)
    print("Inserted record for " + str(result.inserted_id))

args = sys.argv
username = args[1]
passphrase = args[2]

hashed_passphrase = getHashedPassphrase(passphrase)

# print("username = " + username)     #-----dbg!!!
# print("passphrase = " + passphrase)     #-----dbg!!!
# print("hashed_passphrase = " + hashed_passphrase)     #-----dbg!!!

insertIntoDatabase(username, hashed_passphrase)