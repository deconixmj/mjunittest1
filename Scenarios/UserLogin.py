import unittest

from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.LoginPage import Loginpage
from ddt import ddt,data,unpack

@ddt
class UserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        base=Basepage("https://phptravels.net/")
        home=Homepage(base.driver)
        #base.driver.implicitly_wait(10)

        home.click_signin()
        self.Login=Loginpage(base.driver)

        #Login.do_login("rh.mikk-01_01@gmail.com","Rahmi123#")

    def setUp(self):
        pass

    @data(("user@phptravels.com","demouser"))
    @unpack
    def test_user_login(self,username,password):
        self.Login.do_login(username,password)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


# rh.mikk-01_01@gmail.com
# Rahmi123#