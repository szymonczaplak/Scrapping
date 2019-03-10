import time
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver


class Sel():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    def get_images(self):
        driver = self.driver
        driver.get(self.base_url)
        for i in range(1,20):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        soup = BeautifulSoup(data, features="lxml")
        images = []
        for image in soup.find_all("img"):
            images.append(image['src'])
        return images

    def save_files(self, urls):
        counter = 0
        for i in urls:
            urllib.request.urlretrieve(i, "images\\image{}.jpg".format(counter))
            counter += 1


def get_bing_url(name):
    return "https://www.bing.com/images/search?q={}&FORM=HDRSC2".format(name)


wanted_pics = "topless"
url = get_bing_url(wanted_pics)
engine = Sel(url)
images = engine.get_images()

