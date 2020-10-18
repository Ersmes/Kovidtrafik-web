from server import app
from flask import Flask, render_template, request, flash, url_for, redirect
from datetime import datetime
from datetime import date as dt
from datetime import time as tm

import server.getter as getter

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        date = request.form["inputdate"]
        time = request.form["inputtime"]
        
        if date == '' or time == '':
            return redirect('/')

        date_o = dt(int(date[0:4]), int(date[5:7]), int(date[8:]))
        time_o =  tm(hour=int(time[:2]))       

        response = getter.get(date_o, time_o)
        
        return render_template("results.html", response=response)

    else: 
        now = datetime.now()
        max = datetime(2020, 12, 31)
    
        return render_template('index.html', now=now, max=max)

@app.route('/poo')
def poo():
    return "pooooooo"

@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
