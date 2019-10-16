from selenium import webdriver

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.com")

window_main=driver.window_handles[0]
print(window_main)


clientarea=driver.find_element_by_xpath('//a[@href="https://www.phptravels.org"]')
clientarea.click()
window_client=driver.window_handles[1]

print(window_client)
driver.switch_to.window(window_client)

reg=driver.find_element_by_xpath("//a[text()='Register']")
reg.click()

#//a[@href="https://www.phptravels.org/register.php"]