from flask import Flask, render_template, url_for


app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
@app.route('/mainPage/')
def mainPage():

    return render_template('mainPage.html', picture = url_for('static', filename='img/papy4.png'))