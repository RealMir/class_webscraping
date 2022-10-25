import requests
from bs4 import BeautifulSoup
import re

def get_finance_news():
  url = "https://finance.naver.com"
  response = requests.get(url)
  response.raise_for_status()
  soup = BeautifulSoup(response.text,"lxml")
  
  print("\n[경제 뉴스]")
  today_stocks = soup.find_all("span",attrs={"class":re.compile("num_quot")})
  for today_stock in today_stocks:
    print("{}>> " .format(today_stock.parent.parent.a["title"]),end="")
    today_stock = today_stock.find_all("span",attrs={"class":re.compile("num")})
    for stock in today_stock:
      print("{}\t" .format(stock.get_text()), end="")
    print()
    
  major_news = soup.find("h2",attrs={"class":"h_strategy"}).find_next_sibling().find_all("li")
  for num, news in enumerate(major_news, start=1):
    print("{0}. {1}" .format(num,news.get_text().strip()))
    print(f"(링크 : {url+news.a['href']} )")
