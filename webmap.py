import folium

map = folium.Map(location=[33.902075,50.463142])
map.add_child(folium.Marker(location=[33.90,50.47], popup="Hi We are here", icon=folium.Icon(color='green')))
map.save("location.html")
