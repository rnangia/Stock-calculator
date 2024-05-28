from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
import csv
import re
import os
import time
import argparse
from urllib.parse import urlparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--stock", help="Stock")
# parser.add_argument("--get", help="Get Order Book")
# parser.add_argument("--refresh", help="Refresh Order Book")
# args = parser.parse_args()

# stock = args.stock
stock = "CIM"

url = "https://webauthecc.anz.com/oamfed/idp/initiatesso?providerid=CMCShareInvesting"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/jinxedin/Documents/Stocks/code/asx"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=options)
driver.get(url)

time.sleep(1)
driver.find_element_by_id("username").send_keys("xxxx")
driver.find_element_by_id("password").send_keys("xxxx")
driver.find_element_by_class_name("login-button").click()

driver.find_element_by_id("txtOmnibarSearch").send_keys(stock)
driver.find_element_by_id("txtOmnibarSearch").send_keys(Keys.ENTER)
driver.implicitly_wait(1000)
driver.find_element_by_id("_ctl0__ctl0_uiMainSection_idDepthTab").click()
driver.implicitly_wait(1000)

# src = driver.switch_to.frame(driver.find_element_by_xpath('//*[@title="Intentionally Blank"]'))
print("Hello")
buyers = driver.find_elements_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_BuyersTable"]/tbody/tr')
# print(buyers)
for b in range(len(buyers)):
    no_of_buyers = int((driver.find_element_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_BuyersTable"]/tbody/tr[' + str(b+1) +']/td[2]').text).replace(',',''))
    b_volume = int((driver.find_element_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_BuyersTable"]/tbody/tr[' + str(b+1) +']/td[4]').text).replace(',',''))
    bid_price = float(driver.find_element_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_BuyersTable"]/tbody/tr[' + str(b+1) +']/td[6]').text)
    print(no_of_buyers, b_volume, bid_price)

sellers = driver.find_elements_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_SellersTable"]/tbody/tr')
# print(sellers)
for s in range(len(sellers)):
    ask_price = float(driver.find_element_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_SellersTable"]/tbody/tr[' + str(s+1) +']/td[1]/a').text)
    s_volume = int((driver.find_element_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_SellersTable"]/tbody/tr[' + str(s+1) +']/td[2]').text).replace(',',''))
    no_of_sellers = int((driver.find_element_by_xpath('//table[@id="_ctl0__ctl0_uiMainSection_ph_idW_idD_SellersTable"]/tbody/tr[' + str(s+1) +']/td[4]').text).replace(',',''))
    print(ask_price, s_volume, no_of_sellers)

# .get_attribute("src")
# print(src)
# url = urlparse.urljoin(base_url, src)
#
# driver.get(url)
# print(driver.page_source)
