from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(r"Driver/chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://localhost:8080")
driver.implicitly_wait(10)

dispensebutton = driver.find_element(By.XPATH, "//a[contains(text(),'Dispense')]")
red = "#dc3545"

# Verify if button is red
s = dispensebutton.value_of_css_property("background-color")
color = Color.from_string(s).hex
if red == color:
    print("Dispense Button is Red.")

# Verify button text
if dispensebutton.text == "Dispense Now":
    print("Dispense Button text is correct.")

# Verify redirection and text in redirected page
dispensebutton.click()
if "Cash dispense" in driver.page_source:
    print("Redirected successfully and cash dispensed text is correct.")


driver.close()
driver.quit()
