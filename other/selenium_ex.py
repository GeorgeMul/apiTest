import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 使用WebDriver開始瀏覽器會話
driver.get("https://www.google.com")

time.sleep(1)

# 在這裡添加更多網頁自動化操作...
elem = driver.find_element(By.CLASS_NAME, "gLFyf")

elem.send_keys("switch")

time.sleep(1)

elem.send_keys(Keys.ENTER)

input("wait")

# 關閉瀏覽器
driver.quit()