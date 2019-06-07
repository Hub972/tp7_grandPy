#! /usr/bin/env python3
# coding: utf-8
from flask import jsonify
import urllib.request
from io import BytesIO

from grand_py.wiki_pack.wikipy import Wiki
from grand_py.views import app
from grand_py.requests_.api_google import GoogleMapApi

app.config.from_object('config')
def test_json_return(monkeypatch):
    """Test google requests results about a query."""
    results = '7 Cité Paradis, 75010 Paris, France'
    with app.app_context():
        def mockreturn():
            return BytesIO(jsonify(results))
        script = GoogleMapApi()
        req = script.searchAboutQuery(query='openclassrooms', g_key=app.config["G_KEY"] )
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert req[0]['formatted_address'] == results


def test_text_return():
    """Test if wikipedia give a good page about a query"""
    makeWikiSearch = Wiki()
    text = """La cité Paradis est une voie publique située dans le 10e arrondissement de Paris."""
    print(text[0:50])
    wiki = makeWikiSearch.searchContent(query="cité paradis")
    assert wiki[0:50] == text[0:50]

