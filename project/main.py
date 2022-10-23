from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from weather import get_weather

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("headless")
browser = webdriver.Chrome(options=chrome_options)

get_weather(browser)