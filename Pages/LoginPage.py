from Locators.Locators import LoginPageLocators

class Loginpage:

    driver=""
    def __init__(self,d):
        self.driver=d

    def do_login(self,username,password):
        self.driver.find_element(*LoginPageLocators.cookie).click()

        self.driver.implicitly_wait(10)

        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        #self.driver.
        self.driver.find_element(*LoginPageLocators.Login_submit).click()

        #x=self.driver.find_element(*LoginPageLocators.Login_submit)
        #self.driver.execute_script("argument[0].click();",x)




 #frame = self.driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
#self.driver.switch_to.frame(frame)
#self.driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
