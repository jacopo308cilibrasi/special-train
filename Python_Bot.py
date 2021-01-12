
import requests
from pprint import pprint
import time
from datetime import datetime
import json

compito = {
'La valuta con volume_24 maggiore':'',
'Le 10 valute con incremento pecentuale migliore nelle ultime 24h':'',
'Le 10 valute con incremento pecentuale peggiore nelle ultime 24h':'',
'La quantita\' di denaro necessaria per acquistare una unita\' di ciascuna delle prime 20 criptovalute in $':'',
'La quantita\' di denaro necessaria per acquistare una unita\' di tutte le criptovalute, il cui volume delle ultime 24 ore sia superiore a 76.000.000$':'',
'Il Margine di guadagno/perdita in $':'',
'dati' : ''

}

prezzi= []

altreValute = []

prezziOggi = []

percent = []

class Bot:
    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.volume24 = {
            'start' : '1',
            'limit' : '1',
            'convert' : 'USD',
            'sort' : "volume_24h"

        }
        self.top10_per_change_last24= {
            'start': '1',
            'limit': '10',
            'convert': 'USD',
            'percent_change_24h_max' : '10'
        }
        self.last10_per_change_last24= {
            'start': '1',
            'limit': '10',
            'convert': 'USD',
            'percent_change_24h_min': '10'
        }
        self.top_20 = {
            'start': '1',
            'limit': '20',
            'convert': 'USD'
        }
        self.params = {
            'start': '1',
            'limit': '100',
            'convert':'USD'
        }
        self.paramsYesterday = {
            'start': '1',
            'limit':  '20',
            'convert':   'USD',
            'percent_change_24h_max': '20'
        }
        self.headers = {
            'Accepts': 'applications/json',
            'X-CMC_PRO_API_KEY': '318d3bac-1b62-49d8-8ccd-45f2270b0c14'
        }

    def fetchData(self):
        #Cerca la valuta con il Volume maggiore nelle ultime 24 ore
        top24 = requests.get(url=self.url, headers=self.headers, params=self.volume24).json()
        compito['La valuta con volume_24 maggiore'] = top24
        #Cerca le 10 migliori e peggiori valute per incremento percentuale delle ultime 24 ore
        first10 = requests.get(url=self.url, headers=self.headers, params=self.top10_per_change_last24).json()
        compito['Le 10 valute con incremento pecentuale migliore nelle ultime 24h'] = first10
        last10 = requests.get(url=self.url, headers=self.headers, params=self.last10_per_change_last24).json()
        compito['Le 10 valute con incremento pecentuale peggiore nelle ultime 24h'] = last10
        #Cerca le top 20 valute per capitalizzazione e ne calcola il costo complessivo di ciascuna di esse
        top20Valute = requests.get(url=self.url, headers=self.headers, params=self.top_20).json()
        for currency in top20Valute['data']:
            prezzi.append(currency['quote']['USD']['price'])
        laSomma = sum(prezzi)
        compito['La quantita\' di denaro necessaria per acquistare una unita\' di ciascuna delle prime 20 criptovalute in $'] =round(laSomma, 2)
        #Cerca unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$
        #e ne calcola il prezzo complessivo per ciascuna di esse
        valute_topVol = requests.get(url=self.url, headers=self.headers, params=self.params).json()
        for valuta in valute_topVol['data']:
            if valuta['quote']['USD']['volume_24h'] > 76000000:
                altreValute.append(valuta['quote']['USD']['price'])
        totAltreValute = sum(altreValute)
        compito['La quantita\' di denaro necessaria per acquistare una unita\' di tutte le criptovalute, il cui volume delle ultime 24 ore sia superiore a 76.000.000$'] = round(totAltreValute, 2)
        #La percentuale di guadagno o perdita che avreste realizzato se aveste comprato una unità di ciascuna delle prime 20 criptovalute
        # il giorno prima (ipotizzando che la classifca non sia cambiata)
        #Se oggi -> BTC 10000€ +2%
        #Allora ieri -> BTC 10000:102=x:100 ->  100*10000/102 = 9803.92€
        #Con una differenza di -> 196.08€
        top20Valute_Yesterday = requests.get(url=self.url, headers=self.headers, params=self.paramsYesterday).json()
        for cryttoVal in top20Valute_Yesterday['data']:
            percent.append(cryttoVal['quote']['USD']['percent_change_24h'])
            prezziOggi.append(cryttoVal['quote']['USD']['price'])
        iltot = sum(prezziOggi)

        prezziIeritot = 0
        percentcount = 0
        prezziIeri = 0
        for cryptoVal in prezziOggi:
            prezziIeri = cryptoVal *100/ 100 + percent[percentcount]
            prezziIeritot += prezziIeri
            percentcount += 1
        guadagnoOperdita = iltot -prezziIeritot

        compito['Il Margine di guadagno/perdita in $'] = round(guadagnoOperdita, 2)
        compito['dati'] = top20Valute_Yesterday
        #Ciao ho provato ad applicare i suggerimenti
        #
        #
        #Grazie dei consigli


    def scrivi_JSON(self):
        with open('valuta.json', 'w')as outfile:
            json.dump(compito, outfile, indent=4)

        outfile.close()

impactBot = Bot()

while(1):
    now = datetime.now()
    impactBot.__init__()
    impactBot.fetchData()
    impactBot.scrivi_JSON()
    minutes = 1440
    seconds = minutes * 60
    time.sleep(seconds)
