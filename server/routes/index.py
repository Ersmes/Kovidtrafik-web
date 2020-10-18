from server import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/poo')
def poo():
    return "pooooooo"

@app.route('/about')
def about():
    return "about"

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
