import os

print("creating dirs...")

make = ["static", "templates", "static/css"]
dat = """
from flask import *

app = Flask(__name__)

cockie_data = {}

@app.route("/")
def index():
    return render_template("index.html")

app.run()
"""
for i in make:
    os.mkdir(i)

open("templates/index.html", "x")
open("static/css/index.css", "x")
file = open("main.py", "x+")
file.write(dat)
file.close()


print("Done! oyu have a index file and a index css file! plus a main.py file to start your webserver!")
