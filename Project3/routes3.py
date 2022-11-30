from flask import Flask, render_template, request
from finder3 import brewery

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    return render_template("3index.html")

@app.route('/breweries', methods=['POST'])
def breweries():
    place = request.form['City']
    if place == "":
        return render_template("fail.html", fail="No City Name. Plz return to the first page and try again")
    try:
        number = int(request.form['Number'])
    except:
        return render_template("fail.html", fail="No number. Plz return to the first page and try again")
    list0 = brewery(place, number)
    if list0 == "fail":
        return render_template("fail.html", fail="Something went wrong. Either the city doesn't exist or the number of breweries requested is out of range. return to the first page and try again")
    else:   
        return render_template("breweries.html", list=list0)