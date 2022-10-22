from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("headless") # headless mode

def get_agent():
  browser = webdriver.Chrome(options=chrome_options)
  browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
  agent = browser.find_element(By.ID,"detected_value")
  return agent.text

print(f"headlsess agent : {get_agent()}")

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1.2.3.4 Safari/537.36"
chrome_options.add_argument("user-agent="+agent) # add user agent

print(f"add agent option : {get_agent()}")