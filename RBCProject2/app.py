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
        "Jacket_Image": jackets["image"],
        "Jean_Title": jeans["title"],
        "Jean_Image": jeans["image"],
        "Shoes_Title": shoes["title"],
        "Shoes_Image": shoes["image"]
    }

    shopping.update({}, shoppingdict, upsert=True)

    return redirect("/", code = 302)

@app.route("/scrapetwo")
def scrapetwo():
    shopping = mongo.db.shopping

    shorts  = scrape_file.scrape_four()
    polo = scrape_file.scrape_five()
    sandals = scrape_file.scrape_six()

    shoppingdict = {

        "Shorts_Title": shorts["title"],
        "Shorts_Image": shorts["image"],
        "Polo_Title": polo["title"],
        "Polo_Image": polo["image"],
        "Sandals_Title": sandals["title"],
        "Sandals_Image": sandals["image"]
    }

    shopping.update({}, shoppingdict, upsert=True)

    return redirect("/", code = 302)

@app.route("/scrapethree")
def scrapethree():
    shopping = mongo.db.shopping

    dress_shirt  = scrape_file.scrape_seven()
    dress_pant = scrape_file.scrape_eight()
    dress_shoe = scrape_file.scrape_nine()

    shoppingdict = {

        "DShirt_Title": dress_shirt["title"],
        "DShirt_Image": dress_shirt["image"],
        "DP_Title": dress_pant["title"],
        "DP_Image": dress_pant["image"],
        "DS_Title": dress_shoe["title"],
        "DS_Image": dress_shoe["image"]
    }

    shopping.update({}, shoppingdict, upsert=True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)