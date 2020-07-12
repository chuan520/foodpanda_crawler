from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--no-sandbox")
options.add_argument("--headless")


webdriver_path = 'C:\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
driver.get("https://www.foodpanda.com.tw/")
time.sleep(1)

inputAddress = driver.find_element_by_xpath('//*[@id="delivery-information-postal-index"]')
inputAddress.send_keys("新北市泰山區明志路三段145巷34弄10號")
time.sleep(1)

diliveryBtn = driver.find_element_by_xpath('//*[@id="delivery-information-postal-index-form"]/div[2]/button[1]')
diliveryBtn.click()

time.sleep(1)

url = driver.current_url
print(url)

driver.quit()
