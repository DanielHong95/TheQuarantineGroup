import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/covid_data"
# mongo = PyMongo(app)


@app.route("/")
def index():
    result = render_template("index.html")
    return result


@app.route("/get_global_data")
def get_global_data():
    print("hello world")
    return redirect("http://localhost:8000/")


if __name__ == "__main__":
    app.run(debug=True)
