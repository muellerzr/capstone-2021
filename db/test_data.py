from pymongo import MongoClient
from random import randint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://<username>:password@cluster0.27gwi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db=client.credential

#Step 2: Create sample data
usernames = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
passphrases = ['the', 'end', 'is', 'near','im', 'on', 'a', 'boat', 'look', 'at', 'me', 'now', 'splash', '2021']
for x in range(1, 501):
    credentials = {
        'username' : usernames[randint(0, (len(usernames)-1))],
        'passphrase' : passphrases[randint(0, (len(passphrases)-1))] + ' '  + passphrases[randint(0, (len(passphrases)-1))] + ' ' + passphrases[randint(0, (len(passphrases)-1))] + ' ' + passphrases[randint(0, (len(passphrases)-1))] + ' '  + passphrases[randint(0, (len(passphrases)-1))] + ' ' + passphrases[randint(0, (len(passphrases)-1))]
    }

    #Step 3: Insert business object directly into MongoDB via insert_one
    result=db.credentials.insert_one(credentials)

    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
    
#Step 5: Tell us that you are done
print('finished creating 500 users')