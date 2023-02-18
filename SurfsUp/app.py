import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return """Hello, world!
    <br><a href="/api/v1.0/precipitation">Precipitation</a>
    <br><a href="/api/v1.0/stations">Stations</a>
    <br><a href="/api/v1.0/tobs">Tobs</a>
    <br><a href="/api/v1.0/start">Start</a>
    <br><a href="/api/v1.0/range">Range</a>
    """


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    one_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    rain = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > one_year).all()
    session.close()

    all_precipitation = []
    for date, prcp in rain:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_precipitation.append(prcp_dict)

    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    all_stations = session.query(Station.station).all()
    session.close()

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    one_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    active_year = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == "USC00519281").\
    filter(Measurement.date > one_year).all()
    session.close()

    all_temperatures = []
    for date, tobs in active_year:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_temperatures.append(tobs_dict)

    return jsonify(all_temperatures)

@app.route("/api/v1.0/start/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    tmin = session.query(Measurement.date, func.min(Measurement.tobs)).filter(Measurement.date >= start).all()
    tmax = session.query(Measurement.date, func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    tavg = session.query(Measurement.date, func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    since_data = []
    since_dict = {}
    since_dict["min"] = tmin
    since_dict["max"] = tmax
    since_dict["avg"] = tavg
    since_data.append(since_dict)

    return jsonify(since_data)

@app.route("/api/v1.0/<start>/<end>")
def range():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    
    
    session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                            filter(Measurement.date >= start).all()
    session.close()

    all_temperatures = []
    for date, tobs in active_year:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_temperatures.append(tobs_dict)

    return jsonify(all_temperatures)


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)