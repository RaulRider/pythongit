# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:30:03 2017

@author: rrferrero
"""

import urllib.request
import json

#url_trades = 'https://api.bitfinex.com/v1/trades/btcusd'
#url_ticker = 'https://api.bitfinex.com/v1/pubticker/btcusd'
url_kraken = 'https://api.kraken.com/0/public/Assets'

#Just opens de URL, need to .read() to get the information
#trades = urllib.request.urlopen(url_trades)
#ticker = urllib.request.urlopen(url_ticker)
k_get = urllib.request.urlopen(url_kraken) #gets HTTP Response
k_data1 = k_get.read() #reads de response (BYTES)
k_data2 = k_data1.decode('utf-8') #To convert it to a STRING
data = json.loads(k_data2) # reads de STRING and interpretes as JSON format

print(type(k_get))
print(type(k_data1))
print(type(k_data2))
print(type(data))

for pair in data['result']:
    print(pair)
    
    
for pair in data['result']:
    for atribute in pair:
        print(data['result'][pair])
        
        
