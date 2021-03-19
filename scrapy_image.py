from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from urllib import error
from urllib import request
import os
import time

#設定要搜尋的關鍵字
search_key = 'cow photo'

#設定儲存的路徑
imgs_dir = "./images"

#若資料夾不存在則建立
if not os.path.exists(imgs_dir):
    os.mkdir(imgs_dir)

#設定google首頁, 使用的瀏覽器為chrome
url = "https://www.google.com"
explorer = "Chrome"
chromeDriver = 'C:/Users/mnb51/OneDrive/桌面/chromedriver.exe' # chromedriver檔案放的位置
driver = webdriver.Chrome(chromeDriver) 

#開始爬蟲
driver.get(url)

#輸入關鍵字後搜尋, 再選擇圖片的結果
search_input = driver.find_element(By.NAME, 'q')
search_input.clear()
search_input.send_keys(search_key+"\n")
driver.find_element(By.LINK_TEXT, '圖片').click()

#為了抓到更多圖片, 所以要先滾動到底部, 找到頁面最底下的[顯示更多結果]按鈕
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
show_more_button = driver.find_element(By.CSS_SELECTOR, "input[value='顯示更多結果']")

try:
    while True:
        #根據回傳的資訊進行動作, 一直往下滾動到沒有新的內容
        message = driver.find_element(By.CSS_SELECTOR, 'div.OuJzKb.Bqq24e').get_attribute('textContent')
        # print(message)
        if message == '正在載入更多內容，請稍候':
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        elif message == '已成功載入新內容。向下捲動即可閱讀更多內容。':
            # scrolling to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            if show_more_button.is_displayed():
                show_more_button.click()
        elif message == '你已經看完了所有內容':
            break
        elif message == '無法加載更多内容，點擊即可重試。':
            show_more_button.click()
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
except Exception as err:
    print(err)


#抓取頁面中所有CSS定位符號為img.rg_i.Q4LuWd, 也就是影像的tag
imgs = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")
print("共搜尋到{0}張照片, 現在開始下載".format(len(imgs)))

img_count = 0
for img in imgs:
    try:
        print('下載影像 #' + str(img_count) + ':')
        time.sleep(2)
        img_url = img.get_attribute("src")
        if img_url == None:
            continue
            
        path = os.path.join(imgs_dir, str(img_count) + "_img.jpg")
#         request.urlretrieve(url = img_url, filename = path, reporthook = progress_callback, data = None)
        request.urlretrieve(url = img_url, filename = path, data = None)
        img_count = img_count + 1
    except error.HTTPError as http_err:
        print(http_err)
    except Exception as err:
        print(err)