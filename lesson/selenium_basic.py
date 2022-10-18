from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

browser.get(
  "https://www.changwon.ac.kr/portal/na/ntt/selectMainAtNttList.do?mi=14003")
browser.find_element(By.ID, "searchValue").send_keys("english")
browser.find_element(By.XPATH,
                     "//*[@id='srchForm']/fieldset/div/button").click()

browser.find_element(By.ID, "searchValue").clear()
browser.find_element(By.ID, "searchValue").send_keys("toefl")
browser.find_element(
  By.XPATH, "//*[@id='srchForm']/fieldset/div/button").send_keys(Keys.ENTER)

time.sleep(5)
browser.quit()
