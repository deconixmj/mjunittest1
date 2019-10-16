from selenium import webdriver
from datetime import datetime

class Basepage:
    driver=""
    def __init__(self,url):
        self.driver = webdriver.Chrome(r'D:\mjunittest1\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(url)
        #window_main=self.driver.window_handles[0]

    def navigate_back(self):
        self.driver.back()

#b=Basepage("https://phptravels.com")  # instance of the class which creats the initializer - hence launches the url
#b.driver.get()





