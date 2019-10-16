from Locators.Locators import HomePageLocators,HotelBookingLocators

class Hotelbookpage:

    driver=""
    def __init__(self,d):
        self.driver=d

    def click_on_Hotels(self):
        # click "Hotels" from account page. it will bring to home page with hotel booking options.
        self.driver.find_element(*HotelBookingLocators.Hotels).click()

    def HotelSearch(self):

        self.driver.find_element(*HotelBookingLocators.HotelSearch).send_keys("Dubai")       #"cityname or Hotel"
        self.driver.find_element(*HotelBookingLocators.ChooseFromAutofill).click()

        self.driver.find_element(*HotelBookingLocators.CheckIn).click()
        self.driver.find_element(*HotelBookingLocators.DatePickcheckin).click()

        self.driver.find_element(*HotelBookingLocators.CheckOut).click()
        self.driver.find_element(*HotelBookingLocators.DatePickCheckOut).click()

        self.driver.find_element(*HotelBookingLocators.Travellers).click()
        self.driver.find_element(*HotelBookingLocators.ModTravellersAdults).send_keys("4")
        self.driver.find_element(*HotelBookingLocators.ModTravellersChild).send_keys("1")

        self.driver.find_element(*HotelBookingLocators.Submit_Search).click()

    #def HotelBook(self):

     #   self.driver.find_element(*HotelBookingLocators.)

