import requests
from bs4 import BeautifulSoup

url = "https://www.changwon.ac.kr/portal/na/ntt/selectMainAtNttList.do?mi=14003"
header = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

notices = soup.find_all("td", attrs={"class": "ta_l"})
for num, notice in enumerate(notices, start=1):
  regist_day = notice.find_next_siblings()[1].get_text()
  icon = notice.img
  nttSn = notice.a["data-id"]
  link = f"https://www.changwon.ac.kr/portal/na/ntt/selectNttMainAtInfo.do?mi=14003&nttSn={nttSn}"
  if icon != None:
    if "비밀" in icon["alt"]:
      print("!비밀글! ", end="")
  print(
    f"{num}글  제목: {notice.get_text().strip()}  등록일: {regist_day}\n{link}\n")
