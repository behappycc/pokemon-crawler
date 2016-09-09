import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl,random
import json
import coordinate
from time import gmtime, strftime ,sleep

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




p1='https://poke5566.com/pokemons?lat0=25.105680994815224&lng0=121.6160832985505&lat1=25.03228944748724&lng1=121.5729104622468'
p2='https://poke5566.com/pokemons?lat0=25.105680994815224&lng0=121.5729104622468&lat1=25.03228944748724&lng1=121.5297376259431'
p3='https://poke5566.com/pokemons?lat0=25.105680994815224&lng0=121.5297376259431&lat1=25.03228944748724&lng1=121.4865647896394'
p4='https://poke5566.com/pokemons?lat0=25.105680994815224&lng0=121.4865647896394&lat1=25.03228944748724&lng1=121.4433919533357'
p5='https://poke5566.com/pokemons?lat0=25.105680994815224&lng0=121.4433919533357&lat1=25.03228944748724&lng1=121.4002191170320'
p6='https://poke5566.com/pokemons?lat0=25.1790725421432&lng0=121.6160832985505&lat1=25.105680994815224&lng1=121.5729104622468'
p7='https://poke5566.com/pokemons?lat0=25.1790725421432&lng0=121.5729104622468&lat1=25.105680994815224&lng1=121.5297376259431'
p8='https://poke5566.com/pokemons?lat0=25.1790725421432&lng0=121.5297376259431&lat1=25.105680994815224&lng1=121.4865647896394'
p9='https://poke5566.com/pokemons?lat0=25.1790725421432&lng0=121.4865647896394&lat1=25.105680994815224&lng1=121.4433919533357'
p10='https://poke5566.com/pokemons?lat0=25.1790725421432&lng0=121.4433919533357&lat1=25.105680994815224&lng1=121.4002191170320'
p11='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.6160832985505&lat1=24.95889790015926&lng1=121.5729104622468'
p12='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.5729104622468&lat1=24.95889790015926&lng1=121.5297376259431'
p13='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.5297376259431&lat1=24.95889790015926&lng1=121.4865647896394'
p14='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.4865647896394&lat1=24.95889790015926&lng1=121.4433919533357'
p15='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.4433919533357&lat1=24.95889790015926&lng1=121.4002191170320'
p16='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.4002191170320&lat1=24.95889790015926&lng1=121.3570462807283'
p17='https://poke5566.com/pokemons?lat0=25.03228944748724&lng0=121.3570462807283&lat1=24.95889790015926&lng1=121.3138734444246'
p18='https://poke5566.com/pokemons?lat0=24.95889790015926&lng0=121.4002191170320&lat1=24.927295926469974&lng1=121.3570462807283'
p19='https://poke5566.com/pokemons?lat0=24.95889790015926&lng0=121.3570462807283&lat1=24.927295926469974&lng1=121.3138734444246'
pointsList = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19]


##url = 'https://poke5566.com/pokemons?latBL=25.200659&lngBL=121.648051&latTR=24.896521&lngTR=121.178511'

#print (url)


def crawler():
	#while(True):
	i = 0
	text = ''
	random.shuffle(pointsList)
	for p in pointsList:
		while True:
			try:
				url = p
				r = requests.get(url,headers=header,timeout=0.5)

			except requests.exceptions.Timeout:
			    pass
			    # Maybe set up for a retry, or continue in a retry loop
			except requests.exceptions.TooManyRedirects:
			    pass
			    # Tell the user their URL was bad and try a different one
			except requests.exceptions.RequestException as e:
				pass
		    # catastrophic error. bail.
			if str(r) == "<Response [200]>":
				print(p+' OK.')
				break
			else:
				sleep(3)

		sleep(5)
		i += 1

		if i == 1:
			text += r.text.split(']')[0]
		elif i == len(pointsList):
			text += ', '+r.text.split('[')[1]
		elif i > 1 and i<len(pointsList):
			text += ', '+r.text.split(']')[0].split('[')[1]

	data = json.loads(text)

	with open('./pokemon/data '+strftime("%Y-%m-%d-%H-%M-%S", gmtime())+'.json', 'w') as outfile:
	    json.dump(data, outfile,ensure_ascii=False)




#24.96662, 121.178511
#25.009903, 121.648051
#24.896521, 121.287715
#25.200659, 121.430574