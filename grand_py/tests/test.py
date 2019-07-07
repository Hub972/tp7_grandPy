#! /usr/bin/env python3
# coding: utf-8
import requests
import wikipedia


from grand_py.wiki_pack.wikipy import Wiki
from grand_py.requests_.api_google import GoogleMapApi


def test_google_return(monkeypatch):
    """Test google requests results about a query."""
    results = '7 Cité Paradis, 75010 Paris, France'

    def mockreturn(*args, **kwargs):
        return results

    monkeypatch.setattr(requests, 'get', mockreturn)
    script = GoogleMapApi()
    req = script.searchAboutQuery(query='openclassrooms', g_key=1)
    assert req == results


def test_google_bad_return(monkeypatch):
    """Test google requests results about a query."""
    result = '7 Cité Paradis, 75010 Paris, France'
    badResult = 'error'

    def mockreturn(*args, **kwargs):
        return badResult

    monkeypatch.setattr(requests, 'get', mockreturn)
    script = GoogleMapApi()
    req = script.search_about_query(query='open classe room', g_key=1)
    assert req != result


def test_wiki_return(monkeypatch):
    """Test if wikipedia give a good page about a query"""

    url = 'https://fr.wikipedia.org/wiki/Tour_Eiffel'

    def mockreturn(*args, **kwargs):
        return url
    monkeypatch.setattr(wikipedia, 'page', mockreturn)
    makeWikiSearch = Wiki()
    wiki = makeWikiSearch.search_content(query="tour eiffel")
    assert wiki == url


def test_wiki_bad_return(monkeypatch):
    """Test if wikipedia give a good page about a query"""
    url = 'https://fr.wikipedia.org/wiki/Tour_Eiffel'
    bad_url = 'error'

    def mockreturn(*args, **kwargs):
        return bad_url
    monkeypatch.setattr(wikipedia, 'page', mockreturn)
    make_wiki_search = Wiki()
    wiki = make_wiki_search.search_content(query="touf eiffel")
    assert wiki != url


