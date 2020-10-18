from server import app
from flask import Flask, render_template, request, flash, url_for, redirect
from datetime import datetime

import server.modeling as modeling

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        date = request.form["inputdate"]
        time = request.form["inputtime"]
        flash("Processing Date and Time Inputs...")
        
        modeling.predict(time)

        return redirect(url_for("success", day=date, hour=time))
    else: 
        now = datetime.now()
        max = datetime(now.year + 1, now.month, now.day)
    
        return render_template('index.html', now=now, max=max)

@app.route('/success')
def success(day, hour):
    return f"<p>the result crap<p>"

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
