from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("headless")
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(10)

# search apartment
browser.get("https://www.daum.net/")
search = browser.find_element(By.ID,"q")
search.send_keys("동소문동 송산")
search.send_keys(Keys.ENTER)

# switch new tab
browser.find_element(By.CLASS_NAME,"f_tit.tit_place").click()
browser.close()
browser.switch_to.window(browser.window_handles[0])

WebDriverWait(browser, 20).until(
  EC.element_to_be_clickable((By.XPATH,"//div[contains(text(), '매물보기')]/../.."))
).click()

# clicking the no sale can still click
# clicking the sale is error
# So i use try-except
try:
  WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH,"//div[contains(text(), '매물보기')]/../.."))
  ).click()
  print("현재 매물 없음")
except:
  soup = BeautifulSoup(browser.page_source,"lxml")
  houses = soup.find_all("div",attrs={"class":"css-1dbjc4n r-18u37iz r-w3ob7c r-1mi0q7o r-qi0n3 r-c9eks5 r-m611by"})
  for num, house in enumerate(houses, start=1):    
    detail = house.find_all("div",attrs={"class":"css-1563yu1"})
    detail1 = detail[0].get_text()
    detail2 = detail[1].get_text().split("·")
    type = detail1[:2]
    price = detail1[2:]
    area = detail2[0]
    location = detail2[-1]
    boundary = "="*10
    print(f"{boundary} 매물 {num} {boundary}")
    print(f"거래 : {type}")
    print(f"면적 : {area}")
    print(f"가격 : {price}")
    print(f"동,호수 : {location}")

browser.quit()