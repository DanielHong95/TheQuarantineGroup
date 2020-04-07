import import_data
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/covid_data"
mongo = PyMongo(app)


@app.route("/")
def index():
    # mars = mongo.db.mars.find_one()
    # if mars == None:
    #     result = redirect("http://localhost:5000/scrape")
    # else:
    #     result = render_template("index.html", mars=mars)
    result = render_template("index.html")
    return result


@app.route("/get_data")
def insert_data():
    state = mongo.db.state_data
    state_info = import_data.get_state_info()
    state.update_many(
        {"indice": 0, "thread_id": {"$in": state_info}},
        {"$set": {"updated": "yes"}},
        upsert=True,
    )

    us_covid = mongo.db.us_covid_data
    us_covid_info = import_data.get_us_covid_info()
    us_covid.update_many(
        {"indice": 0, "thread_id": {"$in": us_covid_info}},
        {"$set": {"updated": "yes"}},
        upsert=True,
    )

    return redirect("http://localhost:8000/")


if __name__ == "__main__":
    app.run(debug=True)
