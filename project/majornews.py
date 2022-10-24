import requests
from bs4 import BeautifulSoup

def get_major_news():
  header = {"User-Agent": "Mozilla/5.0"}
  response = requests.get("https://news.naver.com/main/officeList.naver",headers=header)
  response.raise_for_status()
  soup = BeautifulSoup(response.text,"lxml")
  
  major_news = soup.find("ul",attrs={"class":"list_txt"})
  top_news = major_news.find_all("li")
  print("[주요 뉴스]")
  for num, news in enumerate(top_news, start=1):
    print("{0}. {1}" .format(num,news.get_text().strip()))
    print(f"(링크 : {news.a['href']})")