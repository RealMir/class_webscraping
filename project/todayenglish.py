import requests
from bs4 import BeautifulSoup
import re

def get_today_english():
  response = requests.get("https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english")
  response.raise_for_status()
  soup = BeautifulSoup(response.text,"lxml")
  
  print("\n[오늘의 영어 회화]")
  li = ["(영어 지문)","(한글 지문)"]
  
  english_texts = soup.find_all("div",attrs={"class":"conv_in"})
  for num,english_text in enumerate(reversed(english_texts)):
    print(li[num])
    today_englishs = english_text.find_all("div",attrs={"id":re.compile("conv_kor")})
    for today_english in today_englishs:
      print(today_english.get_text().strip())