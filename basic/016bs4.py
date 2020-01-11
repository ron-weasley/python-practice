import bs4
import urllib
from bs4 import BeautifulSoup as soup 
# BeautifulSoup does not fetch the web page for you, do that yourself. 
from urllib.request import urlopen

content = urlopen('https://movies-directory.herokuapp.com/').read()

soup_content = soup(content, features='xml')
info = soup_content.find_all("h1",class_ = "card__header")
for title in info:
    print(title.string)