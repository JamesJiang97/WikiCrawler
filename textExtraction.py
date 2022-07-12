import os
from webbrowser import get
from bs4 import BeautifulSoup

def openHtml(path) :

    with open(path, encoding='utf-8') as f :
        html = f.read()
    bs = BeautifulSoup(html, 'html.parser')

    return bs

def getText(bs) :
    div = bs.find('div', class_ = 'mw-parser-output')
    p_list = div.find_all('p')
    for p in p_list : 
        print(p.text)

    # print(p_list)


def main() :
    path = './Portal:史書/史記/史記-卷001/史記-卷001.html'
    bs = openHtml(path)
    getText(bs)


main()



