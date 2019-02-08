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
	fg.add_child ( folium.Marker( location=(lt, ln), popup="Volcano Name: "+na +" & Height:"+str(el)+" m", icon=folium.Icon ( color=color_producter(el)) ) )


map.add_child(fg)

map.save("location.html")