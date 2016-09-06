import json
from os import listdir
from os.path import isfile, join

filePath = './pokemon'
onlyfiles = [join(filePath, f) for f in listdir(filePath) if isfile(join(filePath, f))]

pokeStar = [1,2,3,2,3,4,1,2,3,0,1,2,0,1,2,0,1,2,0,2,0,2,0,2,3,5,
			1,2,1,2,4,1,2,4,1,3,2,4,3,4,0,1,1,2,3,0,2,0,2,2,4,2,
			4,1,3,2,4,3,4,1,2,3,2,3,4,2,3,5,1,2,3,1,2,2,3,4,3,4,
			1,3,2,3,2,1,2,2,4,3,4,2,4,2,3,4,2,2,4,1,2,2,4,2,4,2,
			3,4,4,4,3,4,2,4,5,2,5,2,3,1,3,1,3,5,2,2,3,3,0,5,0,5,
			5,5,1,4,4,4,5,2,4,2,4,4,5,5,5,5,2,3,5,5,5
			]
pokeMonMap = {}




for file in onlyfiles:
	with open(file) as data_file:    
	    data = json.load(data_file)

	for pokemon in data['pokemons']:
		lat = round(pokemon['lat'],6)
		lng = round(pokemon['lng'],6)
		if str((lat,lng)) not in pokeMonMap:
			pokeMonMap[str((lat,lng))] = []
			pokeMonMap[str((lat,lng))].append((pokemon['id'],pokemon['time']))
		else:
			pokeMonMap[str((lat,lng))].append((pokemon['id'],pokemon['time']))

print (len(pokeMonMap.keys()))
for k in pokeMonMap.keys():
	print(pokeMonMap[k],type(k[0]))
	break
while True:
	lat = float(input('lat? :'))
	lng = float(input('lng? :'))
	print (str((lat,lng)))
	if str((lat,lng)) in pokeMonMap:
		print ('here')
		print (pokeMonMap[str((lat,lng))])