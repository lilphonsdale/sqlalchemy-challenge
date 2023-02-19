# sqlalchemy-challenge

<h1>Description</h1>
The jupyter notebook uses SQL alchemy to connect to and query a SQLite database.

Queries return data on precipitation, station activity and temperature observations for a given time frame at the most active station.

The app.py file contains a Flask API which accesses the same database and presents the results of SQLalchemy queries on precipitation, observation stations, and temperature observations. The API also has dynamic routes which take dates in YYYY-MM-DD format and use them to query the SQLite database for minimum, maximum and average temperatures. In the case of /start/ the query searches dates since the given date, for /start/end the query searches the range between the dates. 

<h1>Authors and Acknowledgment</h1>
Thank you instructors, TAs, SQLalchemy, SQLite, Flask, and np.ravel for your magic. 
