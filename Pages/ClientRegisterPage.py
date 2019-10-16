from Locators.Locators import ClientRegisterLocators
from Locators.Locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientRegister:

    driver=""
    def __init__(self,d):
        self.driver=d

    def click_on_clientarea(self):
        y=HomePageLocators.Client_area
        self.waitForElementVisibility(y).click()
        #window_clientarea = self.driver.window_handles[1]
        #self.driver.switch_to.window(window_clientarea)

    def click_on_register(self):
        x=ClientRegisterLocators.Register
        self.waitForElementVisibility(x).click()

    def do_registration(self,firstname,lastname,email,phone,companyname,address1,address2,
                        city,state,pin,country,howfndus,mobile,pwd,cnfpwd):

        self.driver.find_element(*ClientRegisterLocators.FirstName).send_keys(firstname)
        self.driver.find_element(*ClientRegisterLocators.LastName).send_keys(lastname)
        self.driver.find_element(*ClientRegisterLocators.Email).send_keys(email)
        self.driver.find_element(*ClientRegisterLocators.Phone).send_keys(phone)
        self.driver.find_element(*ClientRegisterLocators.CompanyName).send_keys(companyname)
        self.driver.find_element(*ClientRegisterLocators.StreetAddress1).send_keys(address1)
        self.driver.find_element(*ClientRegisterLocators.StreetAddress2).send_keys(address2)
        self.driver.find_element(*ClientRegisterLocators.City).send_keys(city)
        self.driver.find_element(*ClientRegisterLocators.State).send_keys(state)
        self.driver.find_element(*ClientRegisterLocators.Postcode).send_keys(pin)
        self.driver.find_element(*ClientRegisterLocators.Country).send_keys(country)
        self.driver.find_element(*ClientRegisterLocators.HowDFNDUS).send_keys(howfndus)
        self.driver.find_element(*ClientRegisterLocators.Mobile).send_keys(mobile)
        self.driver.find_element(*ClientRegisterLocators.pwd).send_keys(pwd)
        self.driver.find_element(*ClientRegisterLocators.pwd2).send_keys(cnfpwd)

    def finalcaptcha(self):

        frame = self.driver.find_element_by_xpath('//iframe[contains(@src,"recaptcha")]')
        self.driver.switch_to.frame(frame)
        self.driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
        self.driver.find_element(*ClientRegisterLocators.finalreg).click()

    def SubmitRegistration(self):
        self.driver.find_element(*ClientRegisterLocators.finalreg).click()

    def waitForElementVisibility(self,by):
        wait=WebDriverWait(self.driver,25)
        return wait.until(EC.visibility_of_element_located(by))

