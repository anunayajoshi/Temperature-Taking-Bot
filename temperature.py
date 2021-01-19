from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time 
from random import randrange
import datetime as dt
import os



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def temperaturefunction():


    browser.get("https://temptaking.ado.sg/group/e306686f4e962fec4c8b20ea8e60d1fe")

    # select2 = Select(browser.find_element_by_id('meridies-input'))

    # hour = dt.datetime.now().hour

    # if hour == 8:

    #     select2 = Select(browser.find_element_by_id('meridies-input'))
    #     select2.select_by_value('AM')
    # else:
    #     select2 = Select(browser.find_element_by_id('meridies-input'))
    #     select2.select_by_value('PM')
    


    select = Select(browser.find_element_by_id('member-select'))

    select.select_by_value('79563')

    browser.find_element_by_id("ep1").send_keys("//Password//")

    x = randrange(0,9)

    browser.find_element_by_id("td1").send_keys("3")

    browser.find_element_by_id("td2").send_keys("6")


    browser.find_element_by_id("td3").send_keys(x)

    browser.find_element_by_class_name("btn")
    submit = browser.find_element_by_class_name("btn-warning")

    submit.click()

    time.sleep(2)

    subbmit = browser.find_element_by_id("submit-temp-btn")

    subbmit.click()

    
#friend's form 

    browser.get('https://temptaking.ado.sg/group/fbc5d5f18045990d68268126f3a488de')


    select = Select(browser.find_element_by_id('member-select'))

    select.select_by_value('86732')

    browser.find_element_by_id("ep1").send_keys("//Password//")

    x = randrange(0,9)

    browser.find_element_by_id("td1").send_keys("3")

    browser.find_element_by_id("td2").send_keys("6")


    browser.find_element_by_id("td3").send_keys(x)

    browser.find_element_by_class_name("btn")
    submit = browser.find_element_by_class_name("btn-warning")

    submit.click()

    time.sleep(2)

    subbmit = browser.find_element_by_id("submit-temp-btn")

    subbmit.click()



