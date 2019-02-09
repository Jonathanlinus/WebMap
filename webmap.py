import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producter(elevation):
	if elevation < 1000:
		return 'blue'
	elif 1000<= elevation < 3000:
		return 'red'
	else:
		return 'green'

map = folium.Map(location=[42.8799,-113.2210])
fg= folium.FeatureGroup(name="My Map")


for lt, ln, na, el in zip(lat, lon, name, elev):
	fg.add_child ( folium.CircleMarker( location=(lt, ln),radius=10, popup="Volcano Name: "+na +" & Height:"+str(el)+
	" m",fill_color=color_producter(el)) )


fg.add_child(folium.GeoJson(data=(open('world.json', 'r'))))



map.add_child(fg)

map.save("location.html")