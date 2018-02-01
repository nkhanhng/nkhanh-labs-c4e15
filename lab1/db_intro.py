from pymongo import MongoClient

mongo_uri = "mongodb://namkhanh:lioninthewild@ds119688.mlab.com:19688/khanh"

#Open a connection to mlab
client = MongoClient(mongo_uri)

#Get database
db = client.get_default_database()


#retrieve collection
games = db['games']

game_list = games.find()


for game in game_list:
    print(game['title'])


# #creat a new document
# new_blog = {
#     'title': 'Drink',
#     'description': 'Cool'
# }
#
# #put the created document into collection
# blogs.insert_one(new_blog)
