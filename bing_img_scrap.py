import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve

class Sel():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    def get_images(self, explicit_content=False):
        print("Getting images...")
        driver = self.driver
        if explicit_content:
            driver.get("https://www.bing.com/account/general?ru=%2fimages%2fsearch%3fq%3dporn%26qs%3dn%26form%3dQBLH%26scope%3dimages%26sp%3d-1%26pq%3dporn%26sc%3d5-4%26sk%3d%26cvid%3d377FB1D8916E4E048F0A9BC444258C39")
            driver.find_element_by_id("adlt_set_off").click()
            time.sleep(2)
            driver.find_element_by_id("sv_btn").click()
            time.sleep(2)
            driver.find_element_by_id("adlt_confirm").click()

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
        print("Saving...")
        counter = 0
        for adress in urls:
            if re.match("^/", adress):
                continue
            try:
                urlretrieve(adress, "images\\image{}.jpg".format(counter))
            except:
                continue
            counter += 1


def get_bing_url(name):
    return "https://www.bing.com/images/search?q={}&FORM=HDRSC2".format(name)


wanted_pics = "hedgehog"
url = get_bing_url(wanted_pics)
engine = Sel(url)
images = engine.get_images(False)
engine.save_files(images)

