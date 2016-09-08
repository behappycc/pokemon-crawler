import json
from os import listdir
from os.path import isfile, join

filePath = '.\\pokemon'
onlyfiles = [join(filePath, f) for f in listdir(filePath) if isfile(join(filePath, f))]
fileNum = len(onlyfiles)


pokeMonMap = {}
pokeMonCounting =[0]*151

pokemonEn={"1":"Bulbasaur","2":"Ivysaur","3":"Venusaur","4":"Charmander","5":"Charmeleon","6":"Charizard","7":"Squirtle","8":"Wartortle","9":"Blastoise","10":"Caterpie",
"11":"Metapod","12":"Butterfree","13":"Weedle","14":"Kakuna","15":"Beedrill","16":"Pidgey","17":"Pidgeotto","18":"Pidgeot","19":"Rattata","20":"Raticate","21":"Spearow",
"22":"Fearow","23":"Ekans","24":"Arbok","25":"Pikachu","26":"Raichu","27":"Sandshrew","28":"Sandslash","29":"Nidoran♀","30":"Nidorina","31":"Nidoqueen","32":"Nidoran♂",
"33":"Nidorino","34":"Nidoking","35":"Clefairy","36":"Clefable","37":"Vulpix","38":"Ninetales","39":"Jigglypuff","40":"Wigglytuff","41":"Zubat","42":"Golbat","43":"Oddish",
"44":"Gloom","45":"Vileplume","46":"Paras","47":"Parasect","48":"Venonat","49":"Venomoth","50":"Diglett","51":"Dugtrio","52":"Meowth","53":"Persian","54":"Psyduck",
"55":"Golduck","56":"Mankey","57":"Primeape","58":"Growlithe","59":"Arcanine","60":"Poliwag","61":"Poliwhirl","62":"Poliwrath","63":"Abra","64":"Kadabra","65":"Alakazam",
"66":"Machop","67":"Machoke","68":"Machamp","69":"Bellsprout","70":"Weepinbell","71":"Victreebel","72":"Tentacool","73":"Tentacruel","74":"Geodude","75":"Graveler",
"76":"Golem","77":"Ponyta","78":"Rapidash","79":"Slowpoke","80":"Slowbro","81":"Magnemite","82":"Magneton","83":"Farfetch'd","84":"Doduo","85":"Dodrio","86":"Seel",
"87":"Dewgong","88":"Grimer","89":"Muk","90":"Shellder","91":"Cloyster","92":"Gastly","93":"Haunter","94":"Gengar","95":"Onix","96":"Drowzee","97":"Hypno","98":"Krabby",
"99":"Kingler","100":"Voltorb","101":"Electrode","102":"Exeggcute","103":"Exeggutor","104":"Cubone","105":"Marowak","106":"Hitmonlee","107":"Hitmonchan","108":"Lickitung",
"109":"Koffing","110":"Weezing","111":"Rhyhorn","112":"Rhydon","113":"Chansey","114":"Tangela","115":"Kangaskhan","116":"Horsea","117":"Seadra","118":"Goldeen","119":"Seaking",
"120":"Staryu","121":"Starmie","122":"Mr. Mime","123":"Scyther","124":"Jynx","125":"Electabuzz","126":"Magmar","127":"Pinsir","128":"Tauros","129":"Magikarp","130":"Gyarados",
"131":"Lapras","132":"Ditto","133":"Eevee","134":"Vaporeon","135":"Jolteon","136":"Flareon","137":"Porygon","138":"Omanyte","139":"Omastar","140":"Kabuto","141":"Kabutops",
"142":"Aerodactyl","143":"Snorlax","144":"Articuno","145":"Zapdos","146":"Moltres","147":"Dratini","148":"Dragonair","149":"Dragonite","150":"Mewtwo","151":"Mew"}

pokemonZhTw={"Abra":"凱西","Aerodactyl":"化石翼龍","Alakazam":"胡地","Arbok":"阿柏怪","Arcanine":"風速狗","Articuno":"急凍鳥","Beedrill":"大針蜂","Bellsprout":"喇叭芽",
"Blastoise":"水箭龜","Bulbasaur":"妙蛙種子","Butterfree":"巴大蝴","Caterpie":"綠毛蟲","Chansey":"吉利蛋","Charizard":"噴火龍","Charmander":"小火龍","Charmeleon":"火恐龍",
"Clefable":"皮可西","Clefairy":"皮皮","Cloyster":"刺甲貝","Cubone":"可拉可拉","Dewgong":"白海獅","Diglett":"地鼠","Ditto":"百變怪","Dodrio":"嘟嘟利","Doduo":"嘟嘟",
"Dragonair":"哈克龍","Dragonite":"快龍","Dratini":"迷你龍","Drowzee":"素利普","Dugtrio":"三地鼠","Eevee":"伊布","Ekans":"阿柏蛇","Electabuzz":"電擊獸","Electrode":"頑皮彈",
"Exeggcute":"蛋蛋","Exeggutor":"椰蛋樹","Farfetch'd":"大蔥鴨","Fearow":"大嘴雀","Flareon":"火精靈","Gastly":"鬼斯","Gengar":"耿鬼","Geodude":"小拳石","Gloom":"臭臭花",
"Golbat":"大嘴蝠","Goldeen":"角金魚","Golduck":"哥達鴨","Golem":"隆隆岩","Graveler":"隆隆石","Grimer":"臭泥","Growlithe":"卡蒂狗","Gyarados":"暴鯉龍","Haunter":"鬼斯通",
"Hitmonchan":"艾比郎","Hitmonlee":"沙瓦郎","Horsea":"墨海馬","Hypno":"素利柏","Ivysaur":"妙蛙草","Jigglypuff":"胖丁","Jolteon":"雷精靈","Jynx":"迷唇姐","Kabuto":"化石盔",
"Kabutops":"鐮刀盔","Kadabra":"勇吉拉","Kakuna":"鐵殼昆","Kangaskhan":"袋龍","Kingler":"巨鉗蟹","Koffing":"瓦斯彈","Krabby":"大鉗蟹","Lapras":"拉普拉斯","Lickitung":"大舌頭",
"Machamp":"怪力","Machoke":"豪力","Machop":"腕力","Magikarp":"鯉魚王","Magmar":"鴨嘴火龍","Magnemite":"小磁怪","Magneton":"三合一磁怪","Mankey":"猴怪","Marowak":"嘎啦嘎啦",
"Meowth":"喵喵","Metapod":"鐵甲蛹","Mew":"夢幻","Mewtwo":"超夢","Moltres":"火焰鳥","Mr. Mime":"吸盤魔偶","Muk":"臭臭泥","Nidoking":"尼多王","Nidoqueen":"尼多后",
"Nidoran♀":"尼多蘭","Nidoran♂":"尼多朗","Nidorina":"尼多娜","Nidorino":"尼多力諾","Ninetales":"九尾","Oddish":"走路草","Omanyte":"菊石獸","Omastar":"多刺菊石獸",
"Onix":"大岩蛇","Paras":"派拉斯","Parasect":"派拉斯特","Persian":"貓老大","Pidgeot":"比雕","Pidgeotto":"比比鳥","Pidgey":"波波","Pikachu":"皮卡丘","Pinsir":"大甲",
"Poliwag":"蚊香蝌蚪","Poliwhirl":"蚊香君","Poliwrath":"快泳蛙","Ponyta":"小火馬","Porygon":"3D龍","Primeape":"火爆猴","Psyduck":"可達鴨","Raichu":"雷丘",
"Rapidash":"烈焰馬","Raticate":"拉達","Rattata":"小拉達","Rhydon":"鐵甲暴龍","Rhyhorn":"鐵甲犀牛","Sandshrew":"穿山鼠","Sandslash":"穿山王","Scyther":"飛天螳螂",
"Seadra":"海刺龍","Seaking":"金魚王","Seel":"小海獅","Shellder":"大舌貝","Slowbro":"呆河馬","Slowpoke":"呆呆獸","Snorlax":"卡比獸","Spearow":"烈雀",
"Squirtle":"傑尼龜","Starmie":"寶石海星","Staryu":"海星星","Tangela":"蔓藤怪","Tauros":"肯泰羅","Tentacool":"瑪瑙水母","Tentacruel":"毒刺水母","Vaporeon":"水精靈",
"Venomoth":"末入蛾","Venonat":"毛球","Venusaur":"妙蛙花","Victreebel":"大食花","Vileplume":"霸王花","Voltorb":"雷電球","Vulpix":"六尾","Wartortle":"卡咪龜",
"Weedle":"獨角蟲","Weepinbell":"口呆花","Weezing":"雙彈瓦斯","Wigglytuff":"胖可丁","Zapdos":"閃電鳥","Zubat":"超音蝠"}


pokemonStar={"Abra":3,"Aerodactyl":7,"Alakazam":8,"Arbok":5,"Arcanine":8,"Articuno":10,"Beedrill":5,"Bellsprout":1,
"Blastoise":7,"Bulbasaur":2,"Butterfree":5,"Caterpie":0,"Chansey":10,"Charizard":9,"Charmander":3,"Charmeleon":6,
"Clefable":6,"Clefairy":2,"Cloyster":7,"Cubone":2,"Dewgong":7,"Diglett":2,"Ditto":10,"Dodrio":4,"Doduo":1,
"Dragonair":5,"Dragonite":10,"Dratini":3,"Drowzee":3,"Dugtrio":7,"Eevee":1,"Ekans":0,"Electabuzz":6,"Electrode":8,
"Exeggcute":1,"Exeggutor":7,"Farfetch'd":2,"Fearow":5,"Flareon":7,"Gastly":3,"Gengar":8,"Geodude":2,"Gloom":5,
"Golbat":4,"Goldeen":1,"Golduck":6,"Golem":8,"Graveler":5,"Grimer":3,"Growlithe":4,"Gyarados":8,"Haunter":5,
"Hitmonchan":7,"Hitmonlee":7,"Horsea":1,"Hypno":8,"Ivysaur":4,"Jigglypuff":3,"Jolteon":7,"Jynx":4,"Kabuto":3,
"Kabutops":8,"Kadabra":5,"Kakuna":1,"Kangaskhan":10,"Kingler":5,"Koffing":3,"Krabby":1,"Lapras":9,"Lickitung":7,
"Machamp":9,"Machoke":6,"Machop":4,"Magikarp":0,"Magmar":4,"Magnemite":2,"Magneton":7,"Mankey":2,"Marowak":7,
"Meowth":2,"Metapod":1,"Mew":10,"Mewtwo":10,"Moltres":10,"Mr. Mime":10,"Muk":8,"Nidoking":7,"Nidoqueen":7,
"Nidoran♀":1,"Nidoran♂":1,"Nidorina":4,"Nidorino":4,"Ninetales":8,"Oddish":1,"Omanyte":3,"Omastar":8,
"Onix":2,"Paras":1,"Parasect":6,"Persian":7,"Pidgeot":6,"Pidgeotto":3,"Pidgey":0,"Pikachu":5,"Pinsir":1,
"Poliwag":1,"Poliwhirl":4,"Poliwrath":7,"Ponyta":3,"Porygon":9,"Primeape":7,"Psyduck":1,"Raichu":8,
"Rapidash":7,"Raticate":5,"Rattata":0,"Rhydon":7,"Rhyhorn":2,"Sandshrew":1,"Sandslash":6,"Scyther":4,
"Seadra":5,"Seaking":5,"Seel":3,"Shellder":2,"Slowbro":6,"Slowpoke":1,"Snorlax":10,"Spearow":1,
"Squirtle":2,"Starmie":6,"Staryu":1,"Tangela":4,"Tauros":10,"Tentacool":1,"Tentacruel":5,"Vaporeon":7,
"Venomoth":4,"Venonat":1,"Venusaur":7,"Victreebel":7,"Vileplume":7,"Voltorb":3,"Vulpix":3,"Wartortle":4,
"Weedle":0,"Weepinbell":5,"Weezing":8,"Wigglytuff":8,"Zapdos":10,"Zubat":0}

def getCoordinateValue(pokeList):
	value = 0
	pokeMonNum=0
	lastTime =-50
	lastPoke = -1

	for p in pokeList:
		if lastTime != p[2]-1  or lastPoke != p[0]:

			en = pokemonEn[str(p[0])]
			value += pokemonStar[en]
			pokeMonNum+=1
			lastPoke = p[0]
		pokeMonCounting[p[0]] += 1
		lastPoke = p[0]
		lastTime = p[2]

	value/= fileNum
	return value

def printPokemon(l):
	i = 0
	for item in l :
		i+=1
		if pokemonStar[item[3][0]]>0:
			print (item)
		#if i >150:
		#	break

def printTuple(l):
	i = 0
	for item in l :
		i+=1
		print (item)
		if i >150:
			break

def findPoke(pokeMap,pokeID):
	pointList = []
	b = 0
	for ID in pokeID:
		b += pokeMonCounting[ID] 
	b = b / sum(pokeMonCounting)
	print (b)
	for k in pokeMap.keys():
		appear = 0.0
		for pokemon in pokeMap[k]:
			
			if pokemon[0] in pokeID:
				appear+=1.0
		if float(appear/len(pokeMap[k]))/float(len(pokeMap[k])/fileNum) > b:
			pointList.append((k,float(appear/len(pokeMap[k]))*float(len(pokeMap[k])/fileNum)))
	return sorted(pointList, key=lambda tup: tup[1], reverse=True)


for f in onlyfiles:
	with open(f) as data_file:    
	    data = json.load(data_file)
	index = onlyfiles.index(f)
	for pokemon in data['pokemons']:
		lat = round(pokemon['lat'],6)
		lng = round(pokemon['lng'],6)
		en = pokemonEn[str(pokemon['id'])]
		zh = pokemonZhTw[en]
		key = str((lat,lng))
		
		#if pokemonStar[en] > 0:
		if key not in pokeMonMap:
			pokeMonMap[key] = []
		
		pokeMonMap[key].append((pokemon['id'],pokemon['time'],index,(en,zh)))
		
sorting = []
average = 0


for key in pokeMonMap.keys():
	dupFileID = -1
	tobeRemove=[]
	for p in pokeMonMap[key]:

		if p[2] == dupFileID:
			tobeRemove.append(p)

		else:
			dupFileID = p[2]

	for r in tobeRemove:
		pokeMonMap[key].remove(r)

	value =getCoordinateValue(pokeMonMap[key])
	average += value
	sorting.append((key,value))	
	
sortedList = sorted(sorting, key=lambda tup: tup[1], reverse=True)
average = average / len(pokeMonMap.keys())


print ('There are '+str(len(pokeMonMap.keys()))+' pokemons points')
print ('The average value is '+str(average))

#print (maxPoint,pokeMonMap[key],len(pokeMonMap[key]),key)

for i in range(len(sortedList)):
	print (sortedList[i][1]*fileNum)
	printPokemon(pokeMonMap[sortedList[i][0]])
	print ('=============='+sortedList[i][0]+'=================')
	enter = input('press Enter to next')
	if enter == 'exit':
		break

while True:
	
	lat = float(input('lat? :'))
	lng = float(input('lng? :'))
	print (str((lat,lng)))
	if str((lat,lng)) in pokeMonMap:
		value = getCoordinateValue(pokeMonMap[str((lat,lng))])
		printPokemon(pokeMonMap[str((lat,lng))])
	

	pokeID =[int(x) for x in input('ID? :').split()]
	printTuple(findPoke(pokeMonMap,pokeID))