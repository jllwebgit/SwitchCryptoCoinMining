# -*- coding: utf-8 -*-

import numpy
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import os

class Scraping:

    def __init__(self, logdir, url):

        self.crypto = numpy.empty((0,2))
        #ファイル名につける日付
        dateFile = datetime.now().strftime("%Y%m%d-%H%M%S")
        #ログ保存場所
        self.logpath = logdir+dateFile+".csv"
        #スクレイピングするURL
        self.target_url = url

    def ScrapingCrypto(self):

        #URLの指定
        driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
        driver.get(self.target_url)
        html = driver.page_source.encode('utf-8')
        bsObj = BeautifulSoup(html, "html.parser")
        driver.quit()

        #テーブルを指定
        try:
            table = bsObj.findAll("table",{"class":"table table-hover table-vcenter"})[0]
            rows = table.findAll("tr")
        except:
            return(self.crypto)

        #加工
        csvFile = open(self.logpath, 'wt', newline = '', encoding = 'utf-8')
        csvWriter = csv.writer(csvFile)

        try:
            for row in rows:
                if len(row) == 1:
                    continue
                csvRow = []
                for cell in row.findAll(['td', 'th']):
                    csvRow.append(cell.get_text().replace('\n',''))
                csvFile.write(csvRow[0].strip().split(' ')[0]+','+csvRow[8].strip().split(' ')[0]+'\n')
                self.crypto = numpy.append(self.crypto, numpy.array([[csvRow[0].strip().split(' ')[0],csvRow[8].strip().split(' ')[0]]]),axis=0)
        finally:
            csvFile.close()
            return(self.crypto)


