from server import app
from flask import render_template, request, flash, url_for, redirect

@app.route('/')
def hello_world():
    return render_template('index.html', current_date=8)

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        date = request.form["inputdate"]
        time = request.form["inputtime"]
        flash("Processing Date and Time Inputs...")
        return redirect(url_for('success', name=date))
    
@app.route('/success/<name>')
def success(name):
    return "the result crap"

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
