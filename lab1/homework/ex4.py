from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']

customers_list = customers.find()
#-------------------

event = 0
ads = 0
wom = 0


for customer in customers_list:
    if 'events' == customer['ref']:
        event += 1
    elif 'ads' == customer['ref']:
        ads += 1
    elif 'wom' == customer['ref']:
        wom += 1

print ('Event:',event)
print ('Ads:',ads)
print ('Word of world:',wom)

epc = (event / 6969) * 100
apc = (ads / 6969) * 100
wpc = (wom / 6969) * 100

# ------------------
# draw pie chart

part = ['Event','Ads', 'Word of world']
vals = [epc,apc,wpc]

pyplot.pie(vals,labels=part)

pyplot.axis('equal')

pyplot.show()
