from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# @TODO: setup mongo connection
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.store_inventory_db

# @TODO: connect to mongo db and collection


@app.route('/')
def index():
    # Store the entire team collection in a list
    inventory = list(db.store_inventory.find())
    print(inventory)


    # @TODO: render an index.html template and pass it the data you retrieved from the database
    # Return the template with the teams list passed in
    return render_template('index.html', inventory=inventory)


if __name__ == "__main__":
    app.run(debug=True)
