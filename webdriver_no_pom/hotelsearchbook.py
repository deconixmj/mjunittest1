from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#from Locators.MyExceptions import TimeoutException

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.net")


#driver.find_element_by_id("cookyGotItBtn").click()
myacc=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a")
myacc.click()

#login=wait.until(EC.presence_of_element_located((By.XPATH,"(//*[@id='li_myaccount']/ul/li/a)[1]")))

login=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[1]/a")
login.click()

driver.implicitly_wait(7)

driver.find_element_by_id("cookyGotItBtn").click()
driver.find_element_by_name("username").send_keys("user@phptravels.com")
driver.find_element_by_name("password").send_keys("demouser")
#driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[text()='Login']").click()


wait=WebDriverWait(driver,20)
close=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='livechat-eye-catcher']/div[1]")))
close.click()

'''
try:
    wait=WebDriverWait(driver,20)
    close=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='livechat-eye-catcher']/div[1]")))
    close.click()

except TimeoutException:
    pass
'''

wait = WebDriverWait(driver, 15)
wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div[4]/div/div/ul/li[1]/a/text()"),"Demo"))

hotel01 = driver.find_element_by_xpath("//span[contains(text(),'Hotels')]")
hotel01.click()



#hotel01=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Hotels')]")))

## You have to write - wait until the user login is complete.

#hotel01=driver.find_element_by_xpath("//span[contains(text(),'Hotels')]")
#hotel01.click()


#close=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[19]/div[1]")))
#close.click()
#wait1=WebDriverWait(driver,10)

wait=WebDriverWait(driver,15)
hotel02=wait.until(EC.element_to_be_clickable((By.XPATH,"(//a/span[contains(text(),'Search')])[2]")))
hotel02.send_keys("bangalore")

#hotel02.click()
#driver.find_element_by_xpath("/html/body/div[21]/div/input").send_keys("bangalore")

hotel03=driver.find_element_by_xpath('(//div[@class="select2-result-label"])[2]')
hotel03.click()


