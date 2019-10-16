from selenium import webdriver

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.com")

window1=driver.window_handles[0]
login=driver.find_element_by_xpath("//input[@type='submit']")
login.click()
window2=driver.window_handles[1]
driver.switch_to.window(window2)

userid=driver.find_element_by_name("username")
passwd=driver.find_element_by_name("password")

userid.send_keys("rh.mikk-01_01@gmail.com")
passwd.send_keys("Rahmi123#")

## click on captcha
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()

driver.find_element_by_id("login").click()


# you cannot capture a captcha via automation.
