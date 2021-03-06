import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys


class Sel():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True

    def get_images(self, what, scrolls):
        print("Getting images...")
        driver = self.driver

        driver.get(self.base_url)
        input_element = driver.find_element_by_name("q")
        input_element.send_keys(what)
        input_element.send_keys(Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_link_text("Grafika").click()
        for i in range(scrolls):
            if i % 4 == 0 and i > 0:
                try:
                    driver.find_element_by_id("smb").click()
                except:
                    print("No button to click")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        soup = BeautifulSoup(data, features="lxml")
        images = []
        for image in soup.find_all("img"):
            try:
                images.append(image['src'])
            except:
                continue

        return images

    def save_files(self, urls):
        print("Saving...")
        counter = 0
        for adress in urls:
            try:
                urlretrieve(adress, "images\\image{}.jpg".format(counter))
            except:
                continue
            counter += 1


url = "https://www.google.com"
wanted_pics = "hedgehog"
engine = Sel(url)
images = engine.get_images(wanted_pics, 5)
engine.save_files(images)
