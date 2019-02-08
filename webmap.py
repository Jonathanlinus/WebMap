import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])


map = folium.Map(location=[42.8799,-113.2210])

fg= folium.FeatureGroup(name="My Map")

for lt, ln, na in zip(lat, lon, name):
	fg.add_child ( folium.Marker( location=(lt, ln), popup=na, icon=folium.Icon ( color='green' ) ) )

map.add_child(fg)


map.save("location.html")
