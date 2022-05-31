import re
from urllib import response
from wsgiref import headers
import bs4
import os
import urllib

from requests import request



def getHtml(url) :
    head = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    request = urllib.request.Request(url,headers = head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e :
        if hasattr(e, "code") :
            print(e.code)
    
    return html


def mkdir(title) : 
    dir = "./" + title
    cwd = str(os.getcwd())
    if not os.path.exists(dir) and title not in cwd :
        os.makedirs(title)


def getTitle(html) : 
    bs = bs4.BeautifulSoup(html,"html.parser")
    title = str(bs.title.string)
    title = re.sub(r' - .*',"", title)
    return title


def saveHtml(html, title, path) :
    title = path + str(title) + ".html"
    #print(title)
    if not os.path.exists(title) :
        Html_file = open(title,"w")
        Html_file.write(html)
        Html_file.close


def analyzeHtml(path):
     
    file = open(path,"rb")
    html = file.read()
    bs = bs4.BeautifulSoup(html,"html.parser")
    li_list = []
    for ul in bs.find_all("ul", class_=False) :
        for li in ul.find_all("a", attrs = {'href':re.compile("^/wiki/%")}) :
            li_list.append(li)

    return li_list


def process(title) :
    nxtdir = "./" + title
    os.chdir(nxtdir)
    cwd = os.getcwd()
    html = "./" + title + ".html"
    li_list = analyzeHtml(html)
    if li_list != 0 :
        for item in li_list :
            os.chdir(cwd)
            nxturl = "https://zh.wikisource.org" + item["href"]
            print(nxturl)
            nxtitle = item["title"]
            nxtitle = re.sub(r'/', "-", nxtitle)
            print(nxtitle)
            if str(nxtitle) in str(cwd) + title or os.path.exists(nxtitle):
                continue
            mkdir(nxtitle)
            nxtdir = "./" + nxtitle +"/"
            nxthtml = getHtml(nxturl)
            saveHtml(nxthtml, nxtitle, nxtdir)
            process(nxtitle)
            



def main(baseurl) :
    html = getHtml(baseurl)
    title = getTitle(html)
    mkdir(title)
    nxtdir = "./" + title +"/"
    saveHtml(html, title, nxtdir)
    process(title)




main("https://zh.wikisource.org/wiki/Portal:%E5%8F%B2%E6%9B%B8")


