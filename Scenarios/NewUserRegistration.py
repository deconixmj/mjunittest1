import unittest

from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.LoginPage import Loginpage
from Pages.ClientRegisterPage import ClientRegister
from ddt import ddt,data,unpack
from Testdata.read import getUserData,getUserNegativeData

@ddt
class UserRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base=Basepage("https://phptravels.com/")
        cls.window_main=cls.base.driver.window_handles[0]
        cls.reg=ClientRegister(cls.base.driver)
        cls.reg.click_on_clientarea()
        window_clientarea=cls.base.driver.window_handles[1]
        cls.base.driver.switch_to.window(window_clientarea)
        cls.reg.click_on_register()


    def setUp(self):
        pass

    '''@data(*getUserData())
    @unpack
    def test_user_reg(self,fname,lname,Email,phone,company,addr1,addr2,city,state,pin,country,howfndus,mobile,pwd,cnfpwd):
        self.reg.do_registration(fname,lname,Email,phone,company,addr1,addr2,city,state,pin,country,howfndus,mobile,pwd,cnfpwd)
        self.reg.finalcaptcha()

        #assert "
        '''

    @data(*getUserNegativeData())
    @unpack
    def test_user_reg_neg(self,fname,lname,Email,phone,company,addr1,addr2,city,state,pin,country,howfndus,mobile,pwd,cnfpwd):

        self.reg.do_registration(fname, lname, Email, phone, company, addr1,addr2,city,state,pin,country,howfndus,mobile,pwd,cnfpwd)
        #self.reg.finalcaptcha()
        self.reg.SubmitRegistration()

        assert "Please complete the captcha to continue" ==self.base.driver.find_element_by_css_selector("div.alert.alert-danger > ul > li:nth-child(1)").text

    def test_user_reg_weakpwd(self):
        #The password you entered is not strong enough - please enter a more complex password
        #
    def tearDown(self):
        self.base.driver.switch_to.window(self.window_main)

    @classmethod
    def tearDownClass(cls):
        pass

  #"div.alert.alert-danger > ul > li:nth-child(2)").text

# In this test class , I need to click on a captcha and i need to click on cuntry code dropdown and select code

# you have to test negative test cases here, weak password, password not matching, username/email id validation as oer format.
#
