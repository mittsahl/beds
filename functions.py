#!/usr/bin/python3
"""Helper functions"""

import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    """Gets html data"""
    response = requests.get('https://www.ctmentalhealthservices.com/')
    if response.status_code != requests.codes.ok:
        raise RuntimeError("Failure to request to url")
    return response.text

def parse(html):
    """Parses html"""
    tags = []
    soup = bs(html, 'html.parser')
    for tag in soup.find_all("a", {"class" : "std_link"}):
        tags.append(str(tag))
    return tags

def chop(html):
    """Chops it up"""
    return html.split("<span class=\"notranslate\">")

def remove_first_chunk(things):
    """Removes first chunk of unnecessary data"""
    for array in things:
        for strang in array:
            first = strang[0]
            if first.isupper() == False:
                array.remove(strang)


def remove_second_chunk(things, names):
    """Removes second chunk of data"""
    for ting in things:
        for string in ting:
            first = string[0]
            if first.isupper() == True:
                names.append(string)

def remove_last_chunk(names, things):
    """Removes the last chunk of html tags from strings"""
    for name in names:
        strang = name.split("<")
        things.append(strang[0])
    
