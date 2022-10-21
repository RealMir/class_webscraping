from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.implicitly_wait(10)

browser.get("https://twitter.com/explore")
search = browser.find_element(By.XPATH,"//input[@enterkeyhint='search']")
search.send_keys("고양이")
search.send_keys(Keys.ENTER)

def loading_post():
  WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
  )
  
  soup = BeautifulSoup(browser.page_source,"lxml")
  writes = soup.find_all("div",attrs={"data-testid":"tweetText"})
  print(f"find {len(writes)} posts")
  for num, write in enumerate(writes, start=1):
    print(f"{num}글\n {write.text}")
    
loading_post()
y = browser.execute_script("return document.body.scrollHeight") #get height to js
ActionChains(browser).scroll_by_amount(0,y).perform() #scroll action
print("\nafter scroll, ", end="")
loading_post()

browser.quit()