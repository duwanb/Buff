import requests
import lxml.html as lh
#import pandas as pd
import re
import json
import schedule
import time

def job(val, vallucro):
    url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=1&use_suggestion=0&trigger=undefined_trigger&_=1668989390067'
    #cookies = {'session': '1-VoG4H_hshS37D62GV1wg-jY9EMfLTCPlOTopkS_b3AU62036009090'}
    getBuffItems = requests.get(url)
    y = json.loads(getBuffItems.text)
    data = y['data']
    items = data['items']
    filter = '?from=market#tab=selling&sort_by=default'
    
    for item in items:
        ordem = float(item['buy_max_price'])
        min = float(item['sell_min_price'])

        url = 'https://buff.163.com/goods/' + str(item['id']) + filter
        afterfee=min*(0.975)
        lucro=round(((afterfee-ordem))/(ordem)*100,2)
        lucrostr=str(lucro)
        tudo = lucrostr+" | "+ item['market_hash_name'] +" | " + item['buy_max_price']+" | " + item['sell_min_price']
        if (min >= val ):
            if (round(lucro,2)>= vallucro):
                requests.post("https://ntfy.sh/reidasskins",
                data=tudo.encode('utf-8'),
                headers={
                "Click": url
                })
                print(round(lucro,2), item['market_hash_name'], item['buy_max_price'], '|', item['sell_min_price'],  '|', url)

val = input("Digite o minimo: ")
vallucro = input("Digite o lucro: ")

val = int(val)
vallucro = float(vallucro)

schedule.every(5).seconds.do(lambda: job(val, vallucro))


while True:
    schedule.run_pending()
    time.sleep(1)






