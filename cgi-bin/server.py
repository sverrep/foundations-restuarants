from jinja2 import Template

class Restaurant:
    def __init__(self, name, neighborhood):
        self.name = name
        self.neighborhood = neighborhood
    def printr(self):
        return(self.name + ", " + self.neighborhood)


with open("restaurants.txt", "r") as reader:
    restaurants = reader.read().splitlines()
    restaurantlist = []
    i = 0
    orlist = ""
    for x in restaurants:
        info = x.split(",")
        restaurantlist.append(Restaurant(info[0], info[1]))
        orlist = orlist + "<li>" + restaurantlist[i].printr() + "</li>"
        i= i+1

with open("index.html", "w") as writer:
    html1 = Template("""
    <html lang="en"> 
        <head>
            <title>BLN Restaurants</title>
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
            <h1> Restaurants in Berlin </h1>
            <p>
                <ol>
                {{orlist}}
                </ol>
            </p>
        </body>
    </html>""")
    html = html1.render(orlist=orlist)
    writer.write(html)

