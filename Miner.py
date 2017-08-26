# -*- coding: utf-8 -*-

import os
import subprocess
import configparser

config = configparser.ConfigParser()
config.read('Setting.ini')

#マイニングソフトのディレクトリ
_ccminerlyra2v2Directory = config['Miner']['ccminerlyra2v2Directory']
_ccminerDirectory = config['Miner']['ccminerDirectory']
_zecminerDirectory = config['Miner']['zecminerDirectory']
_etherDualMinerDirectory = config['Miner']['etherDualMinerDirectory']

#マイニング開始コマンド
_cmdFTC = config['Miner']['cmdFTC']
_cmdGroestlCoin = config['Miner']['cmdGroestlCoin']
_cmdDigiByte = config['Miner']['cmdDigiByte']
_cmdLBRY = config['Miner']['cmdLBRY']
_cmdNicehash_NeoScrypt = config['Miner']['cmdNicehash_NeoScrypt']

_cmdSIA = config['Miner']['cmdSIA']
_cmdEthash = config['Miner']['cmdEthash']

_cmdMONA = config['Miner']['cmdMONA']
_cmdVTC = config['Miner']['cmdVTC']
_cmdNicehash_Lyra2REv2 = config['Miner']['cmdNicehash_Lyra2REv2']

_cmdZEC = config['Miner']['cmdZEC']
_cmdZCL = config['Miner']['cmdZCL']
_cmdNiceHash_equihash = config['Miner']['cmdNiceHash_equihash']

#各コインのマイニング実行
class StartMining():

    def FTC():
        os.chdir(_ccminerDirectory)
        proc = subprocess.Popen(_cmdFTC.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def GroestlCoin():
        os.chdir(_ccminerDirectory)
        proc = subprocess.Popen(_cmdGroestlCoin.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def DigiByte():
        os.chdir(_ccminerDirectory)
        proc = subprocess.Popen(_cmdDigiByte.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def LBRY():
        os.chdir(_ccminerDirectory)
        proc = subprocess.Popen(_cmdLBRY.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def SIA():
        os.chdir(_etherDualMinerDirectory)
        proc = subprocess.Popen(_cmdSIA.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def MONA():
        os.chdir(_ccminerlyra2v2Directory)
        proc = subprocess.Popen(_cmdMONA.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def VTC():
        os.chdir(_ccminerlyra2v2Directory)
        proc = subprocess.Popen(_cmdVTC.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def ZEC():
        os.chdir(_zecminerDirectory)
        proc = subprocess.Popen(_cmdZEC.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def ZCL():
        os.chdir(_zecminerDirectory)
        proc = subprocess.Popen(_cmdZCL.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def Ethash():
        os.chdir(_etherDualMinerDirectory)
        proc = subprocess.Popen(_cmdEthash.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def NiceHash_equihash():
        os.chdir(_zecminerDirectory)
        proc = subprocess.Popen(_cmdNiceHash_equihash.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def Nicehash_Lyra2REv2():
        os.chdir(_ccminerlyra2v2Directory)
        proc = subprocess.Popen(_cmdNicehash_Lyra2REv2.strip().split(" "),stderr=subprocess.PIPE)
        return proc

    def Nicehash_NeoScrypt():
        os.chdir(_ccminerDirectory)
        proc = subprocess.Popen(_cmdNicehash_NeoScrypt.strip().split(" "),stderr=subprocess.PIPE)
        return proc

