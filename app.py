import pandas as pd
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from db_config import engine, DATABASE


app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/covid_data"
# mongo = PyMongo(app)
Base = automap_base()
Base.prepare(engine, reflect=True)
global_data = Base.classes.global_covid_data
us_data = Base.classes.us_covid_data
us_lookup = Base.classes.us_lookup
session = Session(engine)


@app.route("/")
def index():
    result = render_template("index.html")
    return result


@app.route("/get_global_data")
def get_global_data():
    countries = (
        session.query(global_data.Country_Region)
        .distinct()
        .order_by(global_data.Country_Region)
        .all()
    )
    global_covid_results = (
        session.query(
            global_data.Country_Region,
            global_data.Date,
            func.sum(global_data.Confirmed_Cases),
            func.sum(global_data.Deaths),
            func.sum(global_data.Recovered),
        )
        .group_by(global_data.Country_Region, global_data.Date)
        .order_by(global_data.Country_Region)
    ).all()
    global_covid_dict = [
        {
            "Country": country[0],
            "Country_Data": [
                {
                    "Date": rec[1],
                    "Confirmed_Cases": int(rec[2]),
                    "Deaths": int(rec[3]),
                    "Recovered": int(rec[4]),
                }
                for rec in global_covid_results
                if rec[0] == country[0]
            ],
        }
        for country in countries
    ]
    global_dict = [
        {"Country": r["Country"], "Data": r["Country_Data"][0:]}
        for r in global_covid_dict
    ]
    return jsonify(global_dict)


if __name__ == "__main__":
    app.run(debug=True)
