from selenium import webdriver
import time
import urllib
import os

#set parameters
url = 'https://www.google.com.tw/imghp?hl=zh-TW'

# 啟動chrome瀏覽器
chrome_path = "C:/Users/mnb51/OneDrive/桌面/chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path) 

driver.get(url)
time.sleep(1)

#透過xpath來找到網頁上的指定元件
search_xpath = '/html/body/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input'
search_key = driver.find_element_by_xpath(search_xpath)
search_key.clear()
search_key.send_keys("panda\n")

#點擊
time.sleep(5000)

#關閉視窗
driver.close()