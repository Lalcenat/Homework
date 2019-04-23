# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a string and renders index.html template
# CODE GOES HERE
@app.route("/")
def echo():
    return render_template("index.html", name ="Sally", hobby = "Dancing")

if __name__ == "__main__":
    app.run(debug=True)
