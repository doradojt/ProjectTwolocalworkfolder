import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

engine = create_engine("sqlite:///data.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables

Base.prepare(engine, reflect=True)

# Save reference to the table
Data = Base.classes.data

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
   """List all available api routes."""
   return ("Hi")

@app.route("/names")
def names():

   # Query all station_name
   results = session.query(Data.station_name).all()

   # Convert list of tuples into normal list
   all_names = list(np.ravel(results))

   return jsonify(all_names)

@app.route("/forecastavg")
def forecastavg():

    results = session.query(Data.fcst_avg).all()

    all_avgs = list(np.ravel(results))

    return jsonify(all_avgs)


###@app.route("/alldata")
#def alldata():
#attempt to return all data

 #   results = session.query(Data).all()
 #   data_dict = {}

  #  for data in results:
  #       data_dict["state_id"] = data.state_id
  #       data_dict["station_name"] = data.station_name
  #       data_dict["state"] = data.state
  #       data_dict["country"] = data.country
  #       data_dict["production_date"] = data.production_date
  #       data_dict["forecast_date"] = data.forecast_date
  #       data_dict["lat"] = data.lat
  #       data_dict["lon"] = data.lon
  #       data_dict["fcst_avg"] = data.fcst_avg
   #      data_dict["norm_mn"] = data.norm_mn
   #      data_dict["norm_mx"] = data.norm_mx
   #      data.append(data_dict)
    
   # return jsonify(data_dict)###

   
if __name__ == "__main__":
    app.run(debug=True)