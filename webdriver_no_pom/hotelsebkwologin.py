from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
#from Locators.MyExceptions import TimeoutException

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.net")

def close():
    wait=WebDriverWait(driver,3)
    x=wait.until(EC.visibility_of_element_located((By.XPATH,"//img[@alt='Chat now']")))
    if x is not None:
        hover = ActionChains(driver).move_to_element(x)
        hover.perform()
        return wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="livechat-eye-catcher"]/div[1]'))).click()
    #return

time.sleep(5)

#close()

y=driver.find_element_by_id("cookyGotItBtn")
hover=ActionChains(driver).move_to_element_with_offset(y,1222.890625,559)
hover.click()


#close()

#driver.find_element_by_id("cookyGotItBtn").click()

myacc=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a")
#myacc=driver.find_element_by_xpath("//a[contains(text(),'My Account')]")
myacc.click()

#login=wait.until(EC.presence_of_element_located((By.XPATH,"(//*[@id='li_myaccount']/ul/li/a)[1]")))

login=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[1]/a")

#login=Select(myacc)
#x=login.select_by_visible_text("Login")

login.click()

time.sleep(3)

#driver.find_element_by_id("cookyGotItBtn").click()
driver.find_element_by_name("username").send_keys("user@phptravels.com")
driver.find_element_by_name("password").send_keys("demouser")

y=driver.find_element_by_id("cookyGotItBtn")
hover=ActionChains(driver).move_to_element_with_offset(y,1222.890625,559)
hover.click()


driver.find_element_by_xpath("//button[text()='Login']").click()

time.sleep(5)

hotel01 = driver.find_element_by_xpath("//span[contains(text(),'Hotels')]")
hotel01.click()

driver.find_element_by_xpath('//*[@id="s2id_location"]/a').click()
srch=driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')

#driver.execute_script("arguments[0].click();",srch)

#srch=driver.find_element_by_id("s2id_location")
#driver.execute_script("arguments[0].click();",srch)

srch.send_keys("Bangalore")
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Bangalore']").click()

