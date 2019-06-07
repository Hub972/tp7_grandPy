#! /usr/bin/env python3
# coding: utf-8
import wikipedia


class Wiki:

    def searchContent(self, query):
        """Search a page about a query and select a text for alert"""
        wikipedia.set_lang("fr")
        resultRaw = wikipedia.page(query)
        resultList = resultRaw.content[0:295]
        result = resultList[0]
        print(result)
        return resultList
