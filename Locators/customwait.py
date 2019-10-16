class element_has_text(object):
    def __init__(self,locator,text):
        self.locator=locator
        self.text=text

    def __call__(self, driver):
        element=driver.find_element(*self.locator)
        if self.text in element.text:
            return element
        else:
            return False