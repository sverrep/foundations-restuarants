from jinja2 import Template

# import the python library for SQLite 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT NAME, NEIGHBORHOOD_ID from restaurants")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()
final_list = []
rlist = ""
for x in list_restaurants:
    if x[1] == 1:
        rlist = rlist + "<li>" + x[0] + "</li>"

db_connection.close()

with open("index.html", "w") as writer:
    html1 = Template("""
    <html lang="en"> 
        <head>
            <title>Restaurants in Kreuzberg</title>
        </head>
        <style>
        h1 {
            font-family: sans-serif;
            font-size: 64px;
            color: #000000;
            padding: 5px;
            margin: 5px;
        }
        ul {
            padding: 0;
            margin: 10px;
        }
        li {
            font-family: sans-serif;
            float: left;
            clear: both;
            padding: 5px;   
            margin: 10px;
            border-radius: 5px;
        }
        </style>
        <body>
            <h1> Restaurants in Kreuzberg </h1>
            <p>
            updatepls
                <ol>
                {{rlist}}
                </ol>
            </p>
        </body>
    </html>""")
    html = html1.render(rlist=rlist)
    writer.write(html)

