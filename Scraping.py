# -*- coding: utf-8 -*-

import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('Setting.cfg')

ChromeWebdriverPath = config['Scraping']['ChromeWebdriverPath']


class Scraping:

    def __init__(self, url, *, log_dir=""):
        self.crypto = np.empty((0, 2))
        # ファイル名につける日付
        date_file = datetime.now().strftime("%Y%m%d-%H%M%S")
        # ログ保存場所
        if log_dir == "":
            self.log_path = ""
        else:
            self.log_path = log_dir + date_file + ".csv"
        # スクレイピングするURL
        self.target_url = url

    def scraping_crypto(self):

        # chromeの起動
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=ChromeWebdriverPath, chrome_options=options)
        # データの取得
        driver.get(self.target_url)
        html = driver.page_source.encode('utf-8')
        bs_obj = BeautifulSoup(html, "html.parser")
        driver.quit()

        # テーブルを指定
        try:
            table = bs_obj.findAll("table", {"class": "table table-sm table-hover table-vcenter"})[0]
            rows = table.findAll("tr")
        except:
            return self.crypto

        try:
            for row in rows:
                if len(row) == 1:
                    continue
                csv_row = []
                for cell in row.findAll(['td', 'th']):
                    csv_row.append(cell.get_text().replace('\n', ''))
                self.crypto = np.append(self.crypto, np.array([[csv_row[0].strip().split(' ')[0],
                                                                csv_row[8].strip().split(' ')[0]]]), axis=0)

            # ログ出力
            if self.log_path != "":
                np.savetxt(self.log_path, self.crypto, fmt='%s')

        finally:
            return self.crypto


