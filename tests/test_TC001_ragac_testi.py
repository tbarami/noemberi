from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pytest
import logging

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
@pytest.fixture()
def set_path():
    global driver
    path = "D:\\downkload\\autoimat\\chromedriver.exe"



    driver = Chrome(executable_path=path)
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(5)
    yield
    driver.close()

@pytest.mark.Smoke
def test_page(set_path):

    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms"
    assert driver.current_url == "https://www.thetestingworld.com/testings/"
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,500)")
    obj = Select(driver.find_element_by_id("countryId"))
    obj.select_by_visible_text("Georgia")


    obj2 = Select(driver.find_element_by_id("stateId"))
    obj2.select_by_visible_text("Tbilisi")

    driver.find_element_by_name("fld_email").send_keys("anano@gmail.com")
    log.info
    name("photo5")



    #wait = WebDriverWait(driver,1000)
    #wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"Georgia"))


def name(saxeli):

    driver.get_screenshot_as_file("./venv/images1/" + saxeli + ".jpg")



"""
@pytest.mark.Sanity
def test_page2(set_path):

    driver.get("https://www.thetestingworld.com/")
    driver.maximize_window()

@pytest.mark.Smoke
def test_registracia(set_path):
    driver.get("https://teatri.ge")
    driver.maximize_window()
    
"""


