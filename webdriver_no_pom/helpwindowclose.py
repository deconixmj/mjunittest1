#/html/body/div[19]/div[1]

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("D:\mjunittest1\chromedriver.exe")
driver.maximize_window()
driver.get("https://phptravels.net")

wait=WebDriverWait(driver,15)
close=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[19]/div[1]")))
close.click()



