from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#from Locators.MyExceptions import TimeoutException

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.net")

driver.find_element_by_id("cookyGotItBtn").click()


wait=WebDriverWait(driver,3)
x=wait.until(EC.invisibility_of_element_located((By.XPATH,'//*[@id="livechat-eye-catcher-img"]/img')))
if x:
    driver.find_element_by_xpath('//*[@id="livechat-eye-catcher-img"]/img').click()
    driver.find_element_by_xpath('//*[@id="livechat-eye-catcher"]/div[1]').click()


driver.find_element_by_xpath('//*[@id="s2id_location"]/a').click()
srch=driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')

srch.send_keys("Bangalore")

time.sleep(2)
driver.find_element_by_xpath("//span[text()='Bangalore']").click()

