#!/usr/bin/env python
# coding: utf-8
#-----------------------------------------------------------------
# alcohol_c8y.py
# Read the analog sensor value via MCP3002.
# アルコール濃度を1秒間隔で取得＆アップロードし、60回繰り返して終了する。
# Last udpate: 2016/12/27
# Author: Sho KANEMARU
#-----------------------------------------------------------------
###############
### import module
###############
import spidev
import time
import datetime
import yaml
import requests
import json
import base64
import pprint

# 設定ファイル読み込み
FILEIN_DICT = "config.yml"
f = open(FILEIN_DICT, 'r')
data = yaml.load(f)
f.close()
deviceId = data['deviceId']
userId = data['userId']
password = data['password']
url = data['url']

for num in range(30):
    ### アルコールセンサからアルコール濃度を取得
    spi = spidev.SpiDev()
    spi.open(0, 0)       ###spi ch0
    resp = spi.xfer2([0x68, 0x00])  ###spi ch0
    value = (resp[0] * 256 + resp[1]) & 0x3ff
    alc_val = 1023 - value
    #      print value
    print 'alc: %d' % alc_val

    # 測定日時を取得
    now = datetime.datetime.today()
    currentTime = now.strftime("%Y-%m-%dT%H:%M:%S.000+09:00")

    # HTTPヘッダを設定
    headers = {
        'Content-Type' : 'application/vnd.com.nsn.cumulocity.measurement+json;ver=0.9;charset=UTF-8',
        'Authorization' : 'Basic ' + base64.b64encode(userId + ":" + password),
        'Accept' : "*/*"
    }
    
    # payloadを設定
    payload = {
        "c8y_AlcoholMeasurement": {
            "A": {
                "value": alc_val,
                "unit": "ppm" }
        },
        "time":currentTime,
        "source": {
            "id":deviceId },
        "type": "c8y_AlcoholMeasurement"
    }
    #print headers
    #print payload
    
    # 
    result = requests.post(url + '/measurement/measurements',
                           data = json.dumps(payload),
                           headers = headers)
    print result
    time.sleep(1)
exit

