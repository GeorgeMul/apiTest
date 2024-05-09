import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#打開往google網頁
driver = webdriver.Chrome()
driver.get("https://www.google.com")

#隱性等待回應
driver.implicitly_wait(10)
#定位
elem = driver.find_element(By.CLASS_NAME, "gLFyf")
#輸入
elem.send_keys("呈鎬科技股份有限公司")
#模仿鍵盤按鈕enter
elem.send_keys(Keys.ENTER)
#隱性等待回應
driver.implicitly_wait(10)
#確認第一項定位
driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md").click()



input("wait")