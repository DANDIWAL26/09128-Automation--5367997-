from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/")

srcBtn = driver.find_element(By.NAME, "search_query")
srcBtn.send_keys("india")
srcBtn.send_keys(Keys.ENTER)

srcBtn = driver.find_elements(By.TAG_NAME, "a")

print(len(srcBtn))
count = len(srcBtn)

def test_a():
    expectedvalue = count
    assert 5 <= expectedvalue


'''
if test fails then youtube is displaying less than 5 results and if pass then 5 or more than 5
'''