from Locators.Locators import HomePageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    driver=""
    def __init__(self,d):
        self.driver=d

    def click_signin(self):

        #t=HomePageLocators.Myaccount
        #self.WaitForElementTobeClickable(t).click()

        #self.driver.implicitly_wait(10)
        self.driver.find_element(*HomePageLocators.Myaccount).click()

        #self.driver.implicitly_wait(5)
        '''t=HomePageLocators.Myaccount
        myacc=Select(t)
        myacc.select_by_visible_text("Login")
        '''
        self.driver.find_element(*HomePageLocators.Login).click()

    def WaitForElementTobeClickable(self,by):
        wait=WebDriverWait(self.driver,20)
        return wait.until(EC.element_to_be_clickable(by))

