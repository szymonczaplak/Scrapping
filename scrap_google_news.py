from bs4 import BeautifulSoup
import requests
import urllib.request as u

source = u.urlopen("https://news.google.com/")
soup = BeautifulSoup(source, features="lxml")
for box in soup.find_all("article"):
    if box.h4:
        if box.h4.a.text:
            print(box.h4.a.text)
            link = box.h4.a['href']
            link = link.replace('./', 'https://news.google.com/')
            print("link: {}".format(link))
