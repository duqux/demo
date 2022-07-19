import pytest
import pandas as pd
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# tc008, tc009 & tc010
def test_tc008(browser):
    dispensebutton = browser.find_element("xpath", "//a[contains(text(),'Dispense')]")
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
    if "Cash dispense" in browser.page_source:
        print("Redirected successfully and cash dispensed text is correct.")

