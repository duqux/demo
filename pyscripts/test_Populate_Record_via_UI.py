import pytest
import pandas as pd
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# User Story 3
header_list = ['natid', 'Name', 'gender', 'salary', 'birthday', 'tax']




# tc003 & tc005
def test_tc003(browser):
    path = "D:/pyscripts/test.csv"
    check_header(path)
    URL = 'http://localhost:8080'
    browser.get(URL)
    uploadfile = browser.find_element("xpath", '//input[@type="file"]')
    uploadfile.send_keys(path)


def test_tc006(browser):
    path = "D:/pyscripts/testfail.csv"
    check_header(path)


def check_header(path):
    df = pd.read_csv(path)
    import_headers = df.axes[1]
    print(import_headers)

    assert len(import_headers) == len(header_list)
