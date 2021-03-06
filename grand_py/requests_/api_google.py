#! /usr/bin/env python3
# coding: utf-8
import requests


class GoogleMapApi:

    def search_about_query(self, query, g_key):
        """Search information about a query and select the coordinate"""
        req = requests.get(
            f"""https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={query}%20France&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={g_key}""")
        return req
