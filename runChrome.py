
# Chrome無理やり起動するやつ
# http://qiita.com/hiro-abe/items/cffb3a6a5c145b3b81d9

from selenium import webdriver
import time
import traceback

try:
    dl_folder_path = "ファイルをＤＬするときのパス"
    chromedriver = "chromedriver"
    search_text = "あ"
    chromeOptions = webdriver.ChromeOptions()
    # chromeを起動しサイトへ移動
    driver = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
    driver.get(
        "https://online.nojima.co.jp/Nintendo-HAC-S-KACEA-ESET-%E3%80%90Switch%E3%80%91-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E6%9C%AC%E4%BD%93-%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B32%E3%82%BB%E3%83%83%E3%83%88%EF%BC%885%E5%B9%B4%E4%BF%9D%E8%A8%BC%E3%82%BB%E3%83%83%E3%83%88%EF%BC%89/2810000040986/1/cd/")
    time.sleep(2)
    # 検索窓の取得
  
except Exception as e:
    print(traceback.format_exc())
    driver.close()
    driver.quit()
