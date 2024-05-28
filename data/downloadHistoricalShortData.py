from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from datetime import datetime, timedelta
import csv

start = datetime.strptime('16/06/2010', "%d/%m/%Y")
end = datetime.strptime('30/06/2010', "%d/%m/%Y")
url = "https://asic.gov.au/regulatory-resources/markets/short-selling/short-position-reports-table/"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/jinxedin/Documents/Stocks/data/short/"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=options)
driver.get(url)
driver.implicitly_wait(1000)
elements = driver.find_elements_by_xpath("//section/article")
for e in elements:
    e.click()
    driver.implicitly_wait(500)
    months = e.find_elements_by_xpath("//div[2]/article/div/button")
    for m in months:
        m.click()
        driver.implicitly_wait(1000)
        dates = e.find_elements_by_xpath("//div[2]/article/div[2]/table/tbody/tr/td[3]/a")
        for d in dates:
            driver.execute_script("arguments[0].click();", d)
            driver.implicitly_wait(500)

# for st in (start + timedelta(n) for n in range(1)):
    # fname = "RR%s-001-SSDailyAggShortPos.csv" % st.strftime('%Y%m%d')
    # df = pd.read_csv('https://asic.gov.au/Reports/Daily/%s/%s/%s' % (str(st.year), str(st.month), fname))
    # df.head()
    # df.to_csv(folder + fname)
    # with open(folder + fname, 'w') as f:
        # writer = csv.writer(f)
        # for line in response.iter_lines():
        #     writer.writerow(line.decode('utf-8').split(','))
