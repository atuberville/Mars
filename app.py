#import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import finalscrapewithfunctions

#set up flask
app=Flask(__name__)

#connect to mongo
app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"
mongo=PyMongo(app)

#set up flask routes
@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template("index.html",mars=mars)

#set up scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = finalscrapewithfunctions.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

#run flask
if __name__ == "__main__":
   app.run()