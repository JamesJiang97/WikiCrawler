import os
from bs4 import BeautifulSoup

def openHtml(path) :

    with open(path, encoding='utf-8') as f :
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    return soup




