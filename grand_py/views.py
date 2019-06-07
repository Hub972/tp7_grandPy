#! /usr/bin/env python3
# coding: utf-8
from flask import Flask, render_template, url_for, request, jsonify


from .requests_.api_google import GoogleMapApi
from .wiki_pack.wikipy import Wiki

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
#C req  [{'formatted_address': 'Boulevard de Parc, 77700 Coupvray, France', 'geometry': {'location': {'lat': 48.8671769, 'lng': 2.7838265}, 'viewport': {'northeast': {'lat': 48.86852672989271, 'lng': 2.785176329892722}, 'southwest': {'lat': 48.86582707010727, 'lng': 2.782476670107278}}}, 'name': 'Disneyland Paris', 'opening_hours': {'open_now': False}, 'photos': [{'height': 5333, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/103363958113287360356/photos">Delphine ADAM</a>'], 'photo_reference': 'CmRaAAAAoM4DtCdI0lsWJee2iUqRTz-CI2nQInZl0SyZFku651nbfsLonNYs9cJ3J5ZE3nyrMxOohyuqfhuQc3yrGVki66jVxm9xN1uU0ztMV5w2N6a3qCvFqQw5EfNGE89GczuDEhBtLrWqRgAoouQRLduEBzVVGhS-EfQiOhhztdMdI6G1JG9AAwMOlQ', 'width': 3000}], 'rating': 4.5}]


@app.route('/')
def mainPage():
    """Display the main page"""
    print('mainPage')
    return render_template('mainPage.html', picture=url_for('static', filename='img/papy4.png'))


@app.route('/gRequest/')
def gRequest():
    """Make a google request about a ajax request and return a response in 'ajax_inter.js'"""
    gReq = GoogleMapApi()
    g_key = app.config["G_KEY"]
    query = request.args.get('query')
    print(query)
    reqFilter = gReq.searchAboutQuery(query, g_key)
    print(reqFilter)
    return jsonify(reqFilter)


@app.route('/wRequest/')
def wRequest():
    """Make a wiki search about a ajax request and return a response in 'ajax_inter.js'"""
    wReq = Wiki()
    query = request.args.get('wqueryo')
    wqueryi = wReq.searchContent(query)
    print(wqueryi)
    return jsonify(wqueryi)
