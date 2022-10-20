from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

chrome_option = Options()
chrome_option.add_argument("--no-sandbox")
chrome_option.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=chrome_option)
browser.maximize_window()
browser.implicitly_wait(10)

browser.get("https://flight.naver.com/")

# choose destination
browser.find_element(By.CLASS_NAME,"tabContent_route__1GI8F.select_City__2NOOZ.end").click()
browser.find_elements(By.CLASS_NAME,"autocomplete_Collapse__tP3pM")[1].click()
browser.find_element(By.CLASS_NAME,"autocomplete_Airport__3_dRP").click()

# choose day 
browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
thismonth = datetime.date.today().month
def choose_day(month,day):
  month = month - thismonth
  WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.XPATH,"//b[text()='31']"))
  )
  browser.find_elements(By.XPATH,f"//b[text()='{day}']/..")[month].click()

choose_day(10,31)
choose_day(11,9)

browser.find_element(By.CLASS_NAME,"searchBox_search__2KFn3").click()

WebDriverWait(browser, 20).until(
  EC.presence_of_element_located((By.CLASS_NAME,"concurrent_ConcurrentList__1EKaB"))
)

browser.quit()