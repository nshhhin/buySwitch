
# -*- coding: utf-8 -*-
# buySwitch.py
# by nino
# 現在人気すぎて買えないSwitchをどうにかして買いたい人のためのプログラム

# ノジマオンライン
# ノーマル: https://online.nojima.co.jp/Nintendo-HAC-S-KAAAA-%E3%80%90Switch%E3%80%91-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E6%9C%AC%E4%BD%93-Joy-Con%28L%29-%28R%29-%E3%82%B0%E3%83%AC%E3%83%BC/4902370535709/1/cd/
# スプラ付: https://online.nojima.co.jp/Nintendo-HAC-S-KACEA-%E3%80%90Switch%E3%80%91-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E6%9C%AC%E4%BD%93-%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B32%E3%82%BB%E3%83%83%E3%83%88/4902370537338/1/cd/
# 転売利用禁止!! ダメ絶対!!!

from bs4 import BeautifulSoup #スクレイピング用のライブラリ
import urllib.request
from urllib.request import Request, urlopen

import time
import re

from selenium import webdriver
import time
import traceback

url_normal = "https://online.nojima.co.jp/Nintendo-HAC-S-KAAAA-%E3%80%90Switch%E3%80%91-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E6%9C%AC%E4%BD%93-Joy-Con%28L%29-%28R%29-%E3%82%B0%E3%83%AC%E3%83%BC/4902370535709/1/cd/"
url_spla = "https://online.nojima.co.jp/Nintendo-HAC-S-KACEA-ESET-%E3%80%90Switch%E3%80%91-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E6%9C%AC%E4%BD%93-%E3%82%B9%E3%83%97%E3%83%A9%E3%83%88%E3%82%A5%E3%83%BC%E3%83%B32%E3%82%BB%E3%83%83%E3%83%88%EF%BC%885%E5%B9%B4%E4%BF%9D%E8%A8%BC%E3%82%BB%E3%83%83%E3%83%88%EF%BC%89/2810000040986/1/cd/"
ItemId = "2810000040986" # スプラ版

def main():
	loop = True
	while( loop ):
		time.sleep(1)
		req = Request(url_spla, headers={'User-Agent': 'Mozilla/5.0'})
		response = urlopen(req)
		html = response.read()
		soup = BeautifulSoup(html, "lxml")
		state = soup.find("span", class_="hassoumeyasu2")
		match = re.search('<span>(.*)</span>', str(state))
		print(match.groups()[0]) # => これが「完売御礼」じゃなかった時は在庫がある!!

		if( match.groups()[0] != "完売御礼" ):
			print("入荷したよ!!")
			loop = False
			btnHTML = '<img src="/default/image/btn_large_cart_in2.gif" alt="カートに入れる" onmouseout="this.src=\'/default/image/btn_large_cart_in2.gif\'">'
			btnJS = '<a href="javascript:with(document.forms[\'cart\']){method=\'post\';action=\'/app/catalog/detail/addcart/1/'+ItemId+'/\';if(checkRequired()){submit()}else{dummy();}}">'
			# 入荷したらChromeを開く
			runChrome( url_spla )


# URLを入力しChromeを開く
def runChrome(URL):

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
	  
	except Exception as e:
		print(traceback.format_exc())
		driver.close()
		driver.quit()


if __name__ == '__main__':
	main()

