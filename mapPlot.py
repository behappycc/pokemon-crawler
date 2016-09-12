import gmplot
import numpy as np



path = '.\\plotMap\\'

string = [(25.053595, 121.320341),(25.074114, 121.467265),(24.984233, 121.507514),(25.114402, 121.567549)]

def plot(string,Pokeid):
	gmap = gmplot.GoogleMapPlotter(25.1, 121.5, 11)
	airports = np.asarray(string,dtype=[('lat', np.float32), ('lon', np.float32)])
	#gmap.plot(airports['lat'], airports['lon'], 'cornflowerblue', edge_width=10)
	#gmap.scatter(airports['lat'], airports['lon'], '#3B0B39', size=40, marker=False)
	#gmap.scatter(airports['lat'], airports['lon'], 'k', marker=True)
	gmap.heatmap(airports['lat'], airports['lon'],radius=8)

	gmap.draw(path+str(Pokeid)+"map.html")