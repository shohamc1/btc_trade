import json
import urllib.request
import time
import datetime

url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'

urllib.request.urlretrieve (url, 'data.json')

with open ("data.json") as json_data:
    data = json.load (json_data)

weight = 0

while True:
    #print ("Entered")
    x = data["USD"]
    y = x

    time.sleep (20)
    while True:
        #print ("Entered")
        urllib.request.urlretrieve(url, 'data.json')

        with open("data.json") as json_data:
            data = json.load(json_data)

        x = data["USD"]

        if weight > .5:
            print(datetime.datetime.now().strftime('%H:%M:%S'), "Buy!")
            #print ("Buy!")
        elif weight < -.5:
            print(datetime.datetime.now().strftime('%H:%M:%S'), "Sell!")
            #print ("Sell!")
        break
    if x > y+1:
        weight += 1
    elif  x < y:
        weight -= 1

    #print (x, y)