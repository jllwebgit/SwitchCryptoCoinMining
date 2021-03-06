# -*- coding: utf-8 -*-

from Scraping import Scraping
from Miner import StartMining
import time
import configparser
import os

config = configparser.RawConfigParser()
config.read('Setting.cfg')

# 更新間隔
REFRESH_INTERVAL = 1200

# ログディレクトリ
if config.has_option('SwitchCryptoCoinMining', 'LogDirectory'):
    LogDirectory = config['SwitchCryptoCoinMining']['LogDirectory']
else:
    LogDirectory = ''

# スクレイピング対象のURL
ScrapingURL = config['SwitchCryptoCoinMining']['URL']

# 初期値
NowCoin = ""
proc = ""


while True:
    # スクレイピング
    scrape = Scraping(url=ScrapingURL, log_dir=LogDirectory)
    crypto = scrape.scraping_crypto()

    for i in range(len(crypto)-1):
        # コイン名,%を表示
        print(str(i) + ',' + crypto[i][0] + ',' + crypto[i][1])
        # MiningPoolhub
        # FTC
        if crypto[i][0] == 'Feathercoin(FTC)NeoScrypt':
            if not NowCoin == 'FTC':
                if NowCoin == 'Zcash(ZEC)' or NowCoin == 'ZCL':
                    os.system("taskkill /f /im bminer.exe")
                else:
                    # proc.terminate()
                    os.system("taskkill /f /im ccminer-x64.exe")
                proc = StartMining.FTC()
                NowCoin = 'FTC'
            break
        # Groestlcoin
        elif crypto[i][0] == 'GroestlCoin(GRS)Groestl':
            if not NowCoin == 'GroestlCoin':
                if NowCoin == 'Zcash(ZEC)' or NowCoin == 'ZCL':
                    os.system("taskkill /f /im bminer.exe")
                else:
                    # proc.terminate()
                    os.system("taskkill /f /im ccminer-x64.exe")
                proc = StartMining.GroestlCoin()
                NowCoin = 'GroestlCoin'
            break
        # # LBRY
        # elif crypto[i][0] == 'LBRY(LBC)LBRY':
        #     if not NowCoin == '' and not NowCoin == 'LBRY':
        #         proc.terminate()
        #     if NowCoin == '' or not NowCoin == 'LBRY':
        #         proc = StartMining.LBRY()
        #         NowCoin = 'LBRY'
        #     break
        # # MONA
        # elif crypto[i][0] == 'Monacoin(MONA)Lyra2REv2':
        #     if not NowCoin == '' and not NowCoin == 'MONA':
        #         proc.terminate()
        #     if NowCoin == '' or not NowCoin == 'MONA':
        #         proc = StartMining.MONA()
        #         NowCoin = 'MONA'
        #     break
        # VTC
        elif crypto[i][0] == 'Vertcoin(VTC)Lyra2REv2':
            if not NowCoin == 'VTC':
                if NowCoin == 'Zcash(ZEC)' or NowCoin == 'ZCL':
                    os.system("taskkill /f /im bminer.exe")
                else:
                    # proc.terminate()
                    os.system("taskkill /f /im ccminer-x64.exe")
                proc = StartMining.VTC()
                NowCoin = 'VTC'
            break
        # ZEC
        elif crypto[i][0] == 'Zcash(ZEC)Equihash':
            if not NowCoin == 'Zcash(ZEC)':
                if NowCoin == 'Zcash(ZEC)' or NowCoin == 'ZCL':
                    os.system("taskkill /f /im bminer.exe")
                else:
                    # proc.terminate()
                    os.system("taskkill /f /im ccminer-x64.exe")
                proc = StartMining.ZEC()
                NowCoin = 'Zcash(ZEC)'
            break
        # ZCL
        elif crypto[i][0] == 'Zclassic(ZCL)Equihash':
            if not NowCoin == 'ZCL':
                if NowCoin == 'Zcash(ZEC)' or NowCoin == 'ZCL':
                    os.system("taskkill /f /im bminer.exe")
                else:
                    # proc.terminate()
                    os.system("taskkill /f /im ccminer-x64.exe")
                proc = StartMining.ZCL()
                NowCoin = 'ZCL'
            break
        # # Ethash
        # elif crypto[i][0] == 'Ethereum(ETH)Ethash' or crypto[i][0] == 'EthereumClassic(ETC)Ethash' or crypto[i][0] == 'Expanse(EXP)Ethash':
        #     if not NowCoin == '' and not NowCoin == 'Ethash':
        #         proc.terminate()
        #     if NowCoin == '' or not NowCoin == 'Ethash':
        #         proc = StartMining.Ethash()
        #         NowCoin = 'Ethash'
        #     break
        # # Nicehash-Equihash
        # elif crypto[i][0] == 'Nicehash-EquihashEquihash':
        #     if not NowCoin == '' and not NowCoin == 'Nicehash-Equihash':
        #         proc.send_signal(signal.CTRL_C_EVENT)
        #     if NowCoin == '' or not NowCoin == 'Nicehash-Equihash':
        #         proc = StartMining.NiceHash_equihash()
        #         NowCoin = 'Nicehash-Equihash'
        #     break
        # # Nicehash-Lyra2REv2
        # elif crypto[i][0] == 'Nicehash-Lyra2REv2Lyra2REv2':
        #     if not NowCoin == '' and not NowCoin == 'Nicehash-Lyra2REv2':
        #         proc.terminate()
        #     if NowCoin == '' or not NowCoin == 'Nicehash-Lyra2REv2':
        #         proc = StartMining.Nicehash_Lyra2REv2()
        #         NowCoin = 'Nicehash-Lyra2REv2'
        #     break
        # # Nicehash-NeoScrypt
        # elif crypto[i][0] == 'Nicehash-NeoScryptNeoScrypt':
        #     if not NowCoin == '' and not NowCoin == 'Nicehash-NeoScrypt':
        #         proc.terminate()
        #     if NowCoin == '' or not NowCoin == 'Nicehash-NeoScrypt':
        #         proc = StartMining.Nicehash_NeoScrypt()
        #         NowCoin = 'Nicehash-NeoScrypt'
        #     break
        else:
            i = i + 1

    crypto = ""
    time.sleep(REFRESH_INTERVAL)
