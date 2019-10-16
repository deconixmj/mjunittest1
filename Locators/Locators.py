from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePageLocators:
    #Myaccount=(By.XPATH,'//*[@id="li_myaccount"]/a/text()')
    #Login=(By.XPATH,"//input[@href='https://www.phptravels.net/login']")

    Myaccount=(By.XPATH,"/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a")
    Login=(By.XPATH,"/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[1]/a")

    #Client_area=(By.XPATH,'//a[@href="https://www.phptravels.org"]')

class LoginPageLocators:
    USERNAME=(By.NAME,"username")
    PASSWORD=(By.NAME,"password")

    #Captcha=(By.CSS_SELECTOR,"label.rc-anchor-center-item")
    Login_submit=(By.XPATH,"//button[text()='Login']")
    cookie=(By.ID,"cookyGotItBtn")

class HotelBookingLocators:
    #Hotels=(By.XPATH,"//a[@href='https://www.phptravels.net/m-thhotels']")

    Hotels=(By.XPATH,"//span[contains(text(),'Hotels')]")
    HotelSearch=(By.XPATH,"//a/span[contains(text(),'Search')]")
    CheckIn=(By.NAME,"// input[@name ='checkin']")
    CheckOut=(By.NAME,"//input[@name='checkout']")
    Travellers=(By.NAME,"//input[@name='travellers']")

    # choosing days , default month and year
    # create locators for choosing a future month and year.
    DatePickcheckin=(By.XPATH,'(//div[@class="datepicker-days"]/table/tbody/tr[2]/td[2])[1]')
                              #//div[@class="datepicker-days"]/table/tbody/tr[2]/td[2]')
    DatePickCheckOut=(By.XPATH,'(//div[@class="datepicker-days"]/table/tbody/tr[2]/td[5])[5]')
    ModTravellersAdults=(By.XPATH,"//input[@name='adults']")
    ModTravellersChild=(By.XPATH,"//input[@name='child']")
    ChooseFromAutofill=(By.XPATH,'(//div[@class="select2-result-label"])[2]')
    Submit_Search=(By.XPATH,'(//button[contains(text(),"Search")])[4]')

#class HotelBookingLocators1:


class ClientRegisterLocators:
    Register=(By.XPATH,"//a[text()='Register']")
    FirstName=(By.NAME,'firstname')
    LastName = (By.NAME, 'lastname')
    Email =(By.NAME,'email')
    Phone=(By.NAME,'phonenumber')
    CompanyName = (By.NAME, 'companyname')
    StreetAddress1 = (By.NAME, 'address1')
    StreetAddress2 = (By.NAME, 'address2')
    City = (By.NAME, 'city')
    State = (By.NAME, 'state')
    Postcode = (By.NAME, 'postcode')
    Country= (By.NAME, 'country')
    HowDFNDUS = (By.NAME, 'customfield[1]')
    Mobile = (By.NAME, 'customfield[2]')
    pwd = (By.NAME, 'password')
    pwd2 = (By.NAME, 'password2')
    finalreg=(By.XPATH,"//input[@type='submit']")

              #//input[@value='Register']")

