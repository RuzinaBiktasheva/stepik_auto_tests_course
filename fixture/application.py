from selenium import webdriver
from fixture.helper import Helper
from fixture.session import SessionHelper


class Application():

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.helper = Helper(self)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()