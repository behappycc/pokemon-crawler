

west = 121.14564529501047
east = 121.56329742513742


south = 24.922820333464728
north= 25.211570123879053

p1 = 'lat0=25.015023611161965&lng0=121.5226011739818&lat1=24.941577819123975&lng1=121.50998406277574'
p1 = 'https://poke5566.com/pokemons?lat0=25.063159682692262&lng0=121.61007515035715&lat1=24.989742669892316&lng1=121.49068466268625'


latdiff = 25.063159682692262 - 24.989742669892316
lngdiff = 121.61007515035715  - 121.49068466268625


def getPoints():
	result = []
	pw = west
	pe = pw+lngdiff
	ps = south
	pn = ps+latdiff

	result.append((pw,pe,pn,ps))
	print (latdiff,lngdiff)
	print ((east-west)/lngdiff)
	print ((north-south)/latdiff)

	while True:
		if ps < north:

			upPw = pw
			upPe = pe
			upPn = pn+latdiff
			upPs = pn
			result.append((upPw,upPe,upPn,upPs))
		if pw <east:
			
			leftPw = pe
			leftPe = pe+lngdiff
			leftPn = pn
			leftPs = ps
			result.append((leftPw,leftPe,leftPn,leftPs))

		if pw <east:
			pw = pw+lngdiff
			pe = pe+lngdiff
		if ps <north:
			pn = pn+latdiff
			ps = ps+latdiff

		if pw > east and ps > north:
			break
		else:
			result.append((pw,pe,pn,ps))

	print (result)
	print (len(result))

	return result

if __name__ == '__main__':
	getPoints()