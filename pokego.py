import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import json
from time import gmtime, strftime 

header = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
'Connection':'keep-alive',
'Cookie':'_ga=GA1.2.148654468.1472645061; poke5566=lat0=25.050859100756114&lng0=121.577944525068&lat1=24.97548963093065&lng1=121.50867915946742',
'Host':'poke5566.com',
'Referer':'https://poke5566.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'	
}
url = 'https://poke5566.com/pokemons?latBL=25.037207163945503&lngBL=121.52821451858586&latTR=24.999524019373315&lngTR=121.50332361892765'
print (url)
r = requests.get(url,headers=header,timeout=0.5)

data = json.loads(r.text)

with open('data '+strftime("%Y-%m-%d-%H-%M-%S", gmtime())+'.json', 'w') as outfile:
    json.dump(data, outfile,ensure_ascii=False)
