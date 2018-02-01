from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title': 'Quote',
    'author': 'Nam Khánh',
    'content': 'It is during our darkest moments that we must focus to see the light.-Aristotle'
}

posts.insert_one(new_post)
