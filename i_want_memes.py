import time
import urllib
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

    def get_images(self):
        driver = self.driver
        driver.get(self.base_url)
        for i in range(1,3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        soup = BeautifulSoup(data, features="lxml")
        images = []
        videos = []
        for vid in soup.find_all("div", {"class": "post-view gif-post"}):
            try:
                videos.append(vid.video.source['src'])
            except:
                print("cant append video")
                continue

        for imgs in soup.find_all("picture"):
            try:
                images.append(imgs.img['src'])
            except:
                print("cant append img")
                continue
        return images, videos

    def save_files(self, directory, urls, name, type):
        counter = 0
        for single_url in urls:
            urlretrieve(single_url, "{}\\{}{}.{}".format(directory, name, counter, type))
            counter += 1



base_url = "https://9gag.com/cute"

engine = Sel(base_url)
images_urls, videos_urls = engine.get_images()
engine.save_files("images", images_urls, "image", "jpg")
engine.save_files("videos", videos_urls, "video", "mp4")

