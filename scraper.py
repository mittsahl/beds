#!/usr/bin/python3
"""Scraper for dhmas"""

import sys
import functions as f

def scraper(url):
    """Scraper function"""

    things = []
    names = []
    html = f.get_html(url)
    tags = f.parse(html)
    for tag in tags:
        things.append(f.chop(tag))
    f.remove_first_chunk(things) 
    f.remove_second_chunk(things, names)
    things.clear()
    f.remove_last_chunk(names, things)
    
    for name in things:
        print(name, end="\n\n\n")
        
     

scraper(sys.argv[1])   
