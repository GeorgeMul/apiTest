
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

driver.get("https://google.com")

time.sleep(3)

elem = driver.find_element(By.NAME,"q")

elem.send_keys("hello,selenium")

time.sleep(2)

elem.send_keys(Keys.ENTER)

time.sleep(5)

titles = driver.find_element(By.ID,"search")

driver.quit()