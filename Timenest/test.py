
from database.mongodb import MongoManager

mongo_client = MongoManager("Timenest")


data = {
  "UserID": 1234556,
  "UserName": "christinapatel",
  "Password": "andnfansdnfnausdfn",
  "Calendar": {
    "$oid": "bahsdbfhabhjsdbfhhaf"
  }
}

mongo_client.insert_one(
    'user',
     data
)




