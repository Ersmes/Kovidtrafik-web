from server import app
from flask import Flask, render_template, request, flash, url_for, redirect
from datetime import datetime
from datetime import date as dt
from datetime import time as tm

import server.helpers.kovidtrafik as kovidtrafik

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        date = request.form["inputdate"]
        time = request.form["inputtime"]
        
        date_o = dt(int(date[0:4]), int(date[5:7]), int(date[8:]))

        #response = kovidtrafik.model(date_o, tm(0))
        
        return redirect("/result")

    else: 
        now = datetime.now()
        max = datetime(now.year + 1, now.month, now.day)
    
        return render_template('index.html', now=now, max=max)

@app.route('/result')
def result():
    return render_template("results.html", response="The traffic today is .25 times the normal.")

@app.route('/poo')
def poo():
    return "pooooooo"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict', methods=["POST"])
def predict():
    return "prediction"

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
