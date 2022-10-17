import requests
from bs4 import BeautifulSoup
import xlsxwriter

response = requests.get("https://www.changwon.ac.kr/portal/main.do")
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
banners = soup.find_all('p', class_="popImg")
banner_num = len(banners)
print("{0}개의 배너를 찾았습니다.".format(banner_num))

titles = []
links = []

# 이미지 및 링크 정보등을 추출
for num, banner in enumerate(banners):
  title = banner.parent['title']
  link = banner.parent['href']
  titles.append(title)
  links.append(link)
  img_response = requests.get(banner.img["src"])

  with open(f"info_img/{num}.png", "wb") as f:
    f.write(img_response.content)

# xlsxwriter를 이용해서 엑셀에 이미지와 링크 정보를 저장
workbook = xlsxwriter.Workbook('info.xlsx')
worksheet = workbook.add_worksheet('sheet1')
y = 0
for i in range(banner_num):
  worksheet.insert_image(0, y, f'info_img/{i}.png', {
    'x_scale': 0.2,
    'y_scale': 0.2
  })
  worksheet.write(15, y, "Title")
  worksheet.write(16, y, titles[i])
  worksheet.write(17, y, "Link")
  worksheet.write(18, y, links[i])
  y += 3

workbook.close()