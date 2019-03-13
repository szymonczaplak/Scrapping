import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as u
from selenium.webdriver.common.keys import Keys
from requests import get


def get_emails(search):
    print("Searching emails for question {}".format(search))
    driver = webdriver.Firefox()
    emails = []
    driver.get("https://www.google.com")
    input_element = driver.find_element_by_name("q")
    input_element.send_keys(search)
    input_element.send_keys(Keys.ENTER)
    time.sleep(4)
    source = driver.page_source
    soup = BeautifulSoup(source, features="lxml")
    for link in soup.find_all("div", {"class": "r"}):
        try:
            html = get(link.a.get('href'), headers={'User-Agent': 'Mozilla/5.0'}).text
        except:
            print("skipped")
            continue
        soup = BeautifulSoup(html, "html5lib")
        texts = soup.findAll(text=True)
        for txt in texts:
            match = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", txt)
            if match:
                emails.append(match.group(0))
    #driver.quit()
    return emails


what = "telefony sklep GSM Kraków kontakt email"

emails = get_emails(what)

print(emails)
print(len(emails))
