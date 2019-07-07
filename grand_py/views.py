#! /usr/bin/env python3
# coding: utf-8
from flask import Flask, render_template, url_for, request, jsonify


from .requests_.api_google import GoogleMapApi
from .wiki_pack.wikipy import Wiki

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
def main_page():
    """Display the main page"""
    print('mainPage')
    return render_template('mainPage.html', picture=url_for('static', filename='img/papy4.png'))


@app.route('/gRequest/')
def g_request():
    """Make a google request about a ajax request and return a response in 'ajax_inter.js'"""
    gReq = GoogleMapApi()
    gKey = app.config["G_KEY"]
    query = request.args.get('query')
    print(query)
    req = gReq.search_about_query(query, gKey)
    req = req.json()
    reqFilter = req['candidates']
    print(reqFilter)
    return jsonify(reqFilter)


@app.route('/wRequest/')
def w_request():
    """Make a wiki search about a ajax request and return a response in 'ajax_inter.js'"""
    listReturn = []
    wReq = Wiki()
    query = request.args.get('wqueryo')
    resultRaw = wReq.search_content(query)
    wqueryi = resultRaw.content[0:295]
    pagLink = resultRaw.url
    listReturn.append(wqueryi)
    listReturn.append(pagLink)
    print(listReturn)
    return jsonify(listReturn)
