from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_weather(browser):
  browser.get("https://search.naver.com/search.naver?query=창원날씨")
  soup = BeautifulSoup(browser.page_source,"lxml")
  
  now_weathers = soup.find("div",attrs={"class":"_today"})
  now_weather = now_weathers.find("div",attrs={"class":"temperature_text"}).get_text().strip()
  weather_infos = now_weathers.find("div",attrs={"class":"temperature_info"})
  weather_info = weather_infos.p.get_text()
  
  today_weathers = soup.find("ul",attrs={"class":"week_list"})
  highesttemp = today_weathers.find("span",attrs={"class":"highest"}).get_text()
  lowesttemp = today_weathers.find("span",attrs={"class":"lowest"}).get_text()
  rainfalls = today_weathers.find_all("span",attrs={"class":"weather_left"})
  am_rainfall = rainfalls[0].get_text().strip()
  pm_rainfall = rainfalls[1].get_text().strip()
  
  browser.find_element(By.XPATH,"//strong[text()='미세먼지']").click()
  dust = browser.find_element(By.CLASS_NAME,"state_info._fine_dust._info_layer").text.split("\n")
  ultradust = browser.find_element(By.CLASS_NAME,"state_info._ultrafine_dust._info_layer").text.split("\n")
  browser.quit()
  
  print("[오늘의 날씨]")
  print(weather_info)
  print(f"{now_weather} ({lowesttemp} / {highesttemp})")
  print(f"{am_rainfall.replace(' ',' 강수확률 ')} / {pm_rainfall.replace(' ',' 강수확률 ')}")
  print(f"미세먼지 {dust[-1].replace(' ','㎍/m³ ')}")
  print(f"초미세먼지 {ultradust[-1].replace(' ','㎍/m³ ')}\n")