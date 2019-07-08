#! /usr/bin/env python3
# coding: utf-8


from wikipedia import PageError


from grand_py.wiki_pack.wikipy import Wiki
from grand_py.requests_.api_google import GoogleMapApi


def test_google_return(monkeypatch):
    """Test google requests results about a query."""
    ADD = "7 Cité Paradis, 75010 Paris, France"
    LAT = 48.8748465
    LNG = 2.3504873
    NAME = "openclassrooms"
    RESULTS = {
       "candidates": [
          {
             "formatted_address": ADD,
             "geometry": {
                "location": {
                   "lat": LAT,
                   "lng": LNG
                },

             },
             "name": NAME

          }
       ]

    }

    class MockGet:
        def __init__(self,*args, **kwargs):
            pass

        def json(self):
            return RESULTS

    monkeypatch.setattr('requests.get', MockGet)
    script = GoogleMapApi()
    response = script.search_about_query(query='openclassrooms', g_key=1).json()
    assert response['candidates'][0]['formatted_address'] == ADD


def test_google_bad_return(monkeypatch):
    """Test google requests results about a query."""
    RESULTS = {
       "candidates": [],
       "status": "ZERO_RESULTS"
    }

    class MockGet:
        def __init__(self, *args, **kwargs):
            pass

        def json(self):
            return RESULTS

    monkeypatch.setattr('requests.get', MockGet)
    script = GoogleMapApi()
    response = script.search_about_query(query='kjggdrr', g_key=1).json()
    assert response["status"] != "200 OK"


def test_wiki_return(monkeypatch):
    """Test if wikipedia give a good page about a query"""
    ID = '1359783'
    TITLE = 'Tour Eiffel'
    URL = 'https://fr.wikipedia.org/wiki/Tour_Eiffel'
    RESULT = {
        'pageid': ID,
        'url': URL,
        'title': TITLE
    }

    class MockWiki:
        def __init__(self,*args, **kwargs):
            self.pageId = ID
            self.title = TITLE
            self.url = URL

        def json(self):
            return RESULT

    monkeypatch.setattr('wikipedia.page', MockWiki)
    makeWikiSearch = Wiki()
    response = makeWikiSearch.search_content(query="tour eiffel").json()
    assert response['pageid'] == ID


def test_wiki_bad_return(monkeypatch):
    """ Test if wikipedia give a good page about a query """
    url = 'https://fr.wikipedia.org/wiki/Tour_Eiffel'
    ERROR = PageError
    QUERY = 'jhfddse'

    def mock_return(*args, **kwargs):
        return ERROR
    monkeypatch.setattr('wikipedia.page', mock_return())
    make_wiki_search = Wiki()
    response = make_wiki_search.search_content(query=QUERY)
    assert isinstance(response, PageError)



