# -*- coding: utf-8 -*-

from Scraping import Scraping
from Miner import StartMining
import time
import signal
import io
import configparser

config = configparser.ConfigParser()
config.read('Setting.ini')

#更新間隔
REFRESH_INTERVAL = 1800

#スクレイピング対象のURL
url = 'https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=21.0&factor%5Beth_p%5D=250.0&grof=true&factor%5Bgro_hr%5D=30.0&factor%5Bgro_p%5D=250.0&factor%5Bx11g_hr%5D=8.7&factor%5Bx11g_p%5D=250.0&cn=true&factor%5Bcn_hr%5D=564.0&factor%5Bcn_p%5D=250.0&eq=true&factor%5Beq_hr%5D=350.0&factor%5Beq_p%5D=250.0&lre=true&factor%5Blrev2_hr%5D=30000.0&factor%5Blrev2_p%5D=250.0&ns=true&factor%5Bns_hr%5D=800.0&factor%5Bns_p%5D=250.0&lbry=true&factor%5Blbry_hr%5D=200.0&factor%5Blbry_p%5D=250.0&bk2bf=true&factor%5Bbk2b_hr%5D=1700.0&factor%5Bbk2b_p%5D=250.0&bk14=true&factor%5Bbk14_hr%5D=2650.0&factor%5Bbk14_p%5D=250.0&pas=true&factor%5Bpas_hr%5D=790.0&factor%5Bpas_p%5D=250.0&bkv=true&factor%5Bbkv_hr%5D=5000.0&factor%5Bbkv_p%5D=155.0&factor%5Bcost%5D=0.0&sort=Profit&volume=0&revenue=current&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=&commit=Calculate&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=0&adapt_q_750Ti=0&adapt_q_10606=0&adapt_q_1070=1'

#初期値
NowCoin = ""
proc = ""

while True:
    #スクレイピング
    scrape  = Scraping(config['CryptoCoinMining']['LogDirectory'],url)
    crypto = scrape.ScrapingCrypto()

    for i in range(len(crypto)-1):
        #コイン名,%を表示
        print(str(i) + ',' + crypto[i][0] + ',' + crypto[i][1])
        #MiningPoolhub
        #FTC
        if crypto[i][0] == 'Feathercoin(FTC)':
            if not NowCoin == '' and not NowCoin == 'FTC':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'FTC':
                proc = StartMining.FTC()
                NowCoin = 'FTC'
            break
        #Groestlcoin
        elif crypto[i][0] == 'GroestlCoin(GRS)':
            if not NowCoin == '' and not NowCoin == 'GroestlCoin':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'GroestlCoin':
                proc = StartMining.GroestlCoin()
                NowCoin = 'GroestlCoin'
            break
        #DGB-Groestl(DGB)
        elif crypto[i][0] == 'DGB-Groestl(DGB)':
            if not NowCoin == '' and not NowCoin == 'DigiByte':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'DigiByte':
                proc = StartMining.DigiByte()
                NowCoin = 'DigiByte'
            break
        #LBRY
        elif crypto[i][0] == 'LBRY(LBC)':
            if not NowCoin == '' and not NowCoin == 'LBRY':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'LBRY':
                proc = StartMining.LBRY()
                NowCoin = 'LBRY'
            break
        #SIA
        elif crypto[i][0] == 'Sia(SC)':
            if not NowCoin == '' and not NowCoin == 'SIA':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'SIA':
                proc = StartMining.SIA()
                NowCoin = 'SIA'
            break
        #MONA
        elif crypto[i][0] == 'Monacoin(MONA)':
            if not NowCoin == '' and not NowCoin == 'MONA':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'MONA':
                proc = StartMining.MONA()
                NowCoin = 'MONA'
            break
        #VTC
        elif crypto[i][0] == 'Vertcoin(VTC)':
            if not NowCoin == '' and not NowCoin == 'VTC':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'VTC':
                proc = StartMining.VTC()
                NowCoin = 'VTC'
            break
        #ZEC
        elif crypto[i][0] == 'Zcash(ZEC)':
            if not NowCoin == '' and not NowCoin == 'Zcash(ZEC)':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'Zcash(ZEC)':
                proc = StartMining.ZEC()
                NowCoin = 'Zcash(ZEC)'
            break
        #ZCL
        elif crypto[i][0] == 'Zclassic(ZCL)':
            if not NowCoin == '' and not NowCoin == 'ZCL':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'ZCL':
                proc = StartMining.ZCL()
                NowCoin = 'ZCL'
            break
        #Ethash
        elif crypto[i][0] == 'Ethereum(ETH)' or crypto[i][0] == 'EthereumClassic(ETC)' or crypto[i][0] == 'Expanse(EXP)':
            if not NowCoin == '' and not NowCoin == 'Ethash':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'Ethash':
                proc = StartMining.Ethash()
                NowCoin = 'Ethash'
            break
        #Nicehash-Equihash 
        elif crypto[i][0] == 'Nicehash-Equihash':
            if not NowCoin == '' and not NowCoin == 'Nicehash-Equihash':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'Nicehash-Equihash':
                proc = StartMining.NiceHash_equihash()
                NowCoin = 'Nicehash-Equihash'
            break
        #Nicehash-Lyra2REv2
        elif crypto[i][0] == 'Nicehash-Lyra2REv2':
            if not NowCoin == '' and not NowCoin == 'Nicehash-Lyra2REv2':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'Nicehash-Lyra2REv2':
                proc = StartMining.Nicehash_Lyra2REv2()
                NowCoin = 'Nicehash-Lyra2REv2'
            break
        #Nicehash-NeoScrypt
        elif crypto[i][0] == 'Nicehash-NeoScrypt':
            if not NowCoin == '' and not NowCoin == 'Nicehash-NeoScrypt':
                proc.terminate()
            if NowCoin == '' or not NowCoin == 'Nicehash-NeoScrypt':
                proc = StartMining.Nicehash_NeoScrypt()
                NowCoin = 'Nicehash-NeoScrypt'
            break
        else:
            i = i + 1

    crypto = ""
    time.sleep(REFRESH_INTERVAL)
