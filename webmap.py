import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[42.8799,-113.2210])
fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
	fg.add_child (folium.Marker(location=[lt, ln], popup="Hi This is a Volcano", icon=folium.Icon ( color='green' )))
	
map.add_child(fg)


map.save("location.html")
