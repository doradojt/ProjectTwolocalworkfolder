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
    jeans = scrape_file.scrape_two()
    shoes = scrape_file.scrape_three()

    shoppingdict = {

        "Jacket_Title": jackets["title"],
        "Jacket_Image": jackets["url"],
        "Jean_Title": jeans["title"],
        "Jean_Image": jeans["url"],
        "Shoes_Title": shoes["title"],
        "Shoes_Image": shoes["url"]
    }

    shopping.update({}, shoppingdict, upsert=True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)