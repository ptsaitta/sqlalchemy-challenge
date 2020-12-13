###copy over same dependencies from jupyter notebook, minus matplotlib stuff

import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

###
##import flask, jsonify
###

from flask import Flask, jsonify


###
###set up database and engine, basically same as jupyter notebook
###

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model, reflect tables

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


###
###set up flask
###

app = Flask(__name__)


###
###Make routes
###

#first route is '/', the home page. List all routes available.

@app.route("/")
def home():
    return (
        "This webpage is dedicated to Analysis of the Hawaiian Climate"
        "There are several pages for you to visit:"
        "/api/v1.0/precipitation"
        "/api/v1.0/stations"
        "/api/v1.0/tobs"
        "/api/v1.0/temp/start/end"
    )


# Precipitation route:
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary

@app.route("/api/v1.0/precipitation")
def precipitation():
    prior_year = dt.date(2017, 8, 23 - dt.timedelta(days=365)

    search = session.query(measurement.date, measurement.prcp)
    results_prior_year = search.filter(measurement.date >= prior_year)

    #return JSON representation
    precipitation_dict = {date: prcp for date, prcp in precipitation}
    return jsonify(precipitation_dict)

# Stations route:
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    ###get stations
    stations_query = session.query(station.station).all()

    ###put them in a list (serializable?)

    result = [r[0] for r in stations_query]
    return result



