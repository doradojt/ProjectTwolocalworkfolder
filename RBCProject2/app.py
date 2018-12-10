from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_file

app = Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/project_app"
mongo = PyMongo(app)

@app.route("/")
def echo():

    shopping = mongo.db.shopping.find()
    return render_template("index.html", shopping = shopping)

@app.route("/scrape")
def scrape():
    shopping = mongo.db.shopping

    jackets = scrape_file.scrape_one()

    shoppingdict = {

        "Jacket_Title": jackets["title"],
        "Jacket_Image": jackets["img"]
    }

    jackets.update({}, shoppingdict, upsert=True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)