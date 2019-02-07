import folium

map = folium.Map(location=[33.902075,50.463142])

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[33.90, 50.47], [33.92, 50.49]]:
	fg.add_child (folium.Marker (location=coordinates, popup="Hi We are here", icon=folium.Icon ( color='green' ) ) )

map.add_child(fg)


map.save("location.html")
