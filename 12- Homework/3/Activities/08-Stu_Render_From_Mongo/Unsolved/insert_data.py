import pymongo

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.store_inventory_db


# Creates a collection in the database and inserts two documents
db.store_inventory.insert_many(
    [
        {
            "type": "apples",
            "cost": .23,
            "stock": 333
        },
        {
            "type": "strawberries",
            "cost": .50,
            "stock": 250
        },
        {
            "type": "grapes",
            "cost": .30,
            "stock": 500
         }
    ]
)