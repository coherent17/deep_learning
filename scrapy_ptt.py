import requests
from bs4 import BeautifulSoup

#設定看板名稱
board_name = "Baseball"

#設定url
url = "https://www.ptt.cc/bbs/" + board_name + "/index"
print(url)

#測試看看
page_num = 10010

#發送requests
res = requests.get(url + str(page_num) + ".html")

#看看收到的response是不是200
print(res) 

#把收到的資訊取出來, 存到res_text這個變數
res_text = res.text 

#印出來看看
print(res_text) 

#使用beautifulsoup來整理收到的資訊
res_soup = BeautifulSoup(res_text, "html.parser") 
print(res_soup)