# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)
# @TODO:  Create a route and view function that takes in a list of strings and renders index.html template
# CODE GOES HERE
@app.route("/")
def index():
    team_list = ["Avengers Endgame", "The Color Purple", "Anything with Will Ferrel", "Anything with Zombies"]
    return render_template("index.html", list=team_list)


if __name__ == "__main__":
    app.run(debug=True)
