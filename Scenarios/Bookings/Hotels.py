import unittest

from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.LoginPage import Loginpage
from Pages.HotelBookingPage import Hotelbookpage
from ddt import ddt,data,unpack

@ddt
class Hotelbookcase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        base=Basepage("https://phptravels.net/")
        home=Homepage(base.driver)
        #base.driver.implicitly_wait(10)
        home.click_signin()
        self.Login=Loginpage(base.driver)
        self.Login.do_login("user@phptravels.com","demouser")
        self.hotel=Hotelbookpage(base.driver)
        self.hotel.click_on_Hotels()

    def setUp(self):
        pass

    #@data((,))
    #@unpack
    def test_Hotel_search(self):
        self.hotel.HotelSearch()

    #def test_Hotel_Book(self):
     #   self.hotel.

    def tearDown(self):
        pass
        # logout
        # quit browser.

    @classmethod
    def tearDownClass(cls):
        pass


# rh.mikk-01_01@gmail.com
# Rahmi123#

#Login.do_login("rh.mikk-01_01@gmail.com","Rahmi123#")