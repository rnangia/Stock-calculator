from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

allords = pd.ExcelFile("allords.xlsx")
df = allords.parse("Sheet1")
stocks = df['Stocks'].tolist()

url = "https://webauthecc.anz.com/oamfed/idp/initiatesso?providerid=CMCShareInvesting"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/jinxedin/Documents/Stocks/code/asx"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=options)
driver.get(url)
driver.implicitly_wait(1000)
driver.find_element_by_id("username").send_keys("xxxx")
driver.find_element_by_id("password").send_keys("xxxx")
driver.find_element_by_class_name("login-button").click()
driver.implicitly_wait(1000)
for s in stocks[:1]:
    driver.find_element_by_id("txtOmnibarSearch").send_keys(s)
    driver.find_element_by_id("txtOmnibarSearch").send_keys(Keys.ENTER)
    driver.implicitly_wait(1000)
    driver.find_element_by_id("_ctl0__ctl0_uiMainSection_idPriceHistoryTab").click()
    driver.implicitly_wait(1000)
    select_tf = Select(driver.find_element_by_id("_ctl0__ctl0_uiMainSection_ph_uiDdtimescale"))
    select_tf.select_by_value('all')
    driver.implicitly_wait(1000)
    select_dl = Select(driver.find_element_by_id("_ctl0__ctl0_uiMainSection_ph_exportList"))
    select_dl.select_by_value('csv')
    driver.find_element_by_id("_ctl0__ctl0_uiMainSection_ph_idExportRecords").click()
    driver.implicitly_wait(1000)
