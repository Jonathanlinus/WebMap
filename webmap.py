import folium

map = folium.Map(location=[33.902075,50.463142], zoom_start=13, max_zoom=14, min_zoom=12)
map.save("location.html")
