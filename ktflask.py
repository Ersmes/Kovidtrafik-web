from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        date = request.form["inputdate"]
        time = request.form["inputtime"]
        flash("Date and Time Recorded")
        return redirect(url_for('success', name="something"))

@app.route('/success/<name>')
def success(name):
    return "the result crap"


if __name__ == "__main__":
    app.run(debug=True)