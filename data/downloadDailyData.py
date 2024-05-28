from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
import csv
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
fieldnames = ['Code', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Value', 'Trades']
for s in stocks[:1]:
    driver.find_element_by_id("txtOmnibarSearch").send_keys(s)
    driver.find_element_by_id("txtOmnibarSearch").send_keys(Keys.ENTER)
    driver.implicitly_wait(1000)
    prices = dict()
    # prices = [s,
    #             date.today().strftime("%d/%M/%Y"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_OpeningPrice"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_HighSalePrice"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_LowSalePrice"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_LastPrice"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_TotalVolumeTraded"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_TotalValueTraded"),
    #             driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_TotalTrades")
    #         ]
    prices['Code'] = s
    if date.today().weekday() == 5:
        prices['Date'] = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")
    elif date.today().weekday() == 6:
        prices['Date'] = (date.today() - timedelta(days=2)).strftime("%d/%m/%Y")
    else:
        prices['Date'] = date.today().strftime("%d/%m/%Y")
    prices['Open'] = driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_OpeningPrice").text
    prices['High'] = driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_HighSalePrice").text
    prices['Low'] = driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_LowSalePrice").text
    prices['Close'] = driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_LastPrice").text
    prices['Volume'] = (driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_TotalVolumeTraded").text).replace(',', '')
    prices['Value'] = driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_TotalValueTraded").text.replace(',', '')
    prices['Trades'] = driver.find_element_by_id("_ctl0__ctl0_uiMainSection_InstrumentQuotePrices_TotalTrades").text.replace(',', '')


    with open("/Users/jinxedin/Documents/Stocks/code/asx/" + s + ".csv", 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(prices)
