#encoding:utf-8
import sys
from datetime import time
from selenium import webdriver
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import csv

#创建浏览器对象
driver = webdriver.Chrome(service=Service(r'chromedriver.exe'))
driver.implicitly_wait(10)
# get方法会一直等到页面被完全加载,然后才会继续程序,通常测试会在这里选择 time.sleep(2)
driver.get("https://www.boc.cn/sourcedb/whpj/")
driver.maximize_window()
#获取输入
date = input("请输入日期：")
str = input("请输入币种：")
#判断日期合法
try:
    if len(date) != 8:
        raise ValueError("输入长度不是八位，请重新输入")

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])

    if year < 2001 or year > 2024:
        raise ValueError("年份范围应该在2001-2024之间")

    if month < 1 or month > 12:
        raise ValueError("月份范围应该在1到12之间")

    if day < 1 or day > 31:
        raise ValueError("日期范围应该在1到31之间")
    print("输入的日期合法")
except ValueError as e:
    print("输入的日期不合法：", e)
    sys.exit()
# 获取输入框
key1 = driver.find_element(By.ID,"erectDate")
key2 = driver.find_element(By.ID,"nothing")
key1.send_keys(date)
key2.send_keys(date)
#币种转换
currency="0"
if str == "GBP":
    currency = "英镑"
elif str == "HKD":
    currency = "港币"
elif str == "USD":
    currency = "美元"
elif str == "HKD":
    currency = "瑞士法郎"
elif str == "SGD":
    currency = "新加坡元"
elif str == "SEK":
    currency = "瑞典克朗"
elif str == "DKK":
    currency = "丹麦克朗"
elif str == "NOK":
    currency = "挪威克朗"
elif str == "JPY":
    currency = "日元"
elif str == "CAD":
    currency = "加拿大元"
elif str == "AUD":
    currency = "澳大利亚元"
elif str == "EUR":
    currency = "欧元"
elif str == "MOP":
    currency = "澳门元"
elif str == "PHP":
    currency = "菲律宾比索"
elif str == "THP":
    currency = "泰国铢"
elif str == "NZD":
    currency = "新西兰元"
elif str == "KPW":
    currency = "韩元"
elif str == "SUR":
    currency = "卢布"
elif str == "MYR":
    currency = "林吉特"
elif str == "TWB":
    currency = "新台币"
elif str == "ESP":
    currency = "西班牙比塞塔"
elif str == "ITL":
    currency = "意大利里拉"
elif str == "NLG":
    currency = "荷兰盾"
elif str == "BEF":
    currency = "比利时法郎"
elif str == "FIM":
    currency = "芬兰马克"
elif str == "IDR":
    currency = "印尼卢比"
elif str == "BRC":
    currency = "巴西里亚尔"
elif str == "AED":
    currency = "阿联酋迪拉姆"
elif str == "INR":
    currency = "印度卢比"
elif str == "ZAR":
    currency = "南非兰特"
elif str == "SAR":
    currency = "沙特里亚尔"
elif str == "TRL":
    currency = "土耳其里拉"
else:
    # 判断合法
    print("无此币种")
    sys.exit()

#读取选项框
select = Select(driver.find_element(By.ID, "pjname"))
select.select_by_value(currency)
#点击搜
check = driver.find_element(By.CSS_SELECTOR,"#historysearchform .search_btn")
check.click()
#获取目录
#tagNames = driver.find_elements(By.CSS_SELECTOR, "th")
#for element in tagNames:
#    print(element.get_attribute('outerHTML'))
#获取数据nth-of-child
Num = driver.find_element(By.CSS_SELECTOR, ".odd td:nth-of-type(4)")
outPut = Num.text
print(outPut)
#存储
f = open("d:/test.csv", 'a')
writer = csv.writer(f)
writer.writerow([date,str,"现汇卖出价",outPut])
f.close()
input()