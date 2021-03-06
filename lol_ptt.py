from selenium import webdriver

#chromedriver.exe執行檔所存在的路徑, 這邊請用你自己的路徑
chrome_path = "C:/Users/mnb51/OneDrive/桌面/chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

#輸入範例網址，交給瀏覽器
driver.get('http://pala.tw/js-example/')   

#取得網頁原始碼
pageSource = driver.page_source  
print(pageSource)

#關閉瀏覽器
driver.close() 