import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"Driver/chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://localhost:8080")
driver.implicitly_wait(10)

uploadfile = driver.find_element_by_class('custom-file-input')
uploadfile.send_keys("test.csv")
driver.close()
driver.quit()