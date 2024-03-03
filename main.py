from selenium import webdriver
#from selenium.webserver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#创建浏览器对象
driver = webdriver.Chrome(service=Service(r'chromedriver.exe'))

#get
driver.get("http://www.baidu.com/")

kw=driver.find_element(By.ID,"kw")
kw.send_keys("长城")

su=driver.find_element(By.CSS_SELECTOR,"#su")
su.click()
input()