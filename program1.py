from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")

src = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
src.send_keys("india")
src.send_keys(Keys.ENTER)

src = driver.find_elements(By.TAG_NAME, "a")

#time.sleep(10)
print(len(src))
cnt = len(src)



def test_a():
    expectedvalue = cnt
    assert 10 <= expectedvalue

'''
if test fails then google is displaying less than 10 results and if pass then 5 or more than 5
'''
