from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.net")

driver.implicitly_wait(10)

#driver.find_element_by_xpath('//*[@id="livechat-eye-catcher"]/div[1]').click()

driver.find_element_by_id("cookyGotItBtn").click()
wait=WebDriverWait(driver,20)
myacc=wait.until(EC.presence_of_element_located((By.XPATH,"//div/ul/li[@id='li_myaccount']/a")))
driver.execute_script("arguments[0].click();",myacc)

#myacc=driver.find_element_by_css_selector('#li_myaccount > a')
# (//*[@id='li_myaccount']/a)[1]"
#myacc=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a")
#myacc.click()
#login=wait.until(EC.presence_of_element_located((By.XPATH,"(//*[@id='li_myaccount']/ul/li/a)[1]")))
#login=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[1]/a")
#login.click()

