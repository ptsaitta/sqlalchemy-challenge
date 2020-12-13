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