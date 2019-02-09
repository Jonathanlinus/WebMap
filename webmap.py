import folium
import pandas
import json
import codecs

data = pandas.read_csv ( "Volcanoes.txt" )
lat = list ( data["LAT"] )
lon = list ( data["LON"] )
name = list ( data["NAME"] )
elev = list ( data["ELEV"] )


def color_producter(elevation):
	if elevation < 1000:
		return 'blue'
	elif 1000 <= elevation < 3000:
		return 'red'
	else:
		return 'green'


map = folium.Map ( location=[42.8799, -113.2210], zoom_start=6, tiles="Mapbox Bright" )

fgv = folium.FeatureGroup ( name="Volcanoes" )

for lt, ln, na, el in zip ( lat, lon, name, elev ):
	fgv.add_child (
		folium.CircleMarker ( location=(lt, ln), radius=6, popup="Volcano Name: " + na + " & Height:" + str ( el ) +
		                                                         " m", fill_color=color_producter ( el ), color='grey',
		                      fill_opacity=0.7 ) )

fgp = folium.FeatureGroup ( name="Population" )

fgp.add_child ( folium.GeoJson ( open ( "world.json", 'r', encoding="utf-8-sig" ).read (),
                                style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'} ) )
map.add_child ( fgv )
map.add_child( fgp )
map.add_child(folium.LayerControl())

map.save ( "location.html" )
