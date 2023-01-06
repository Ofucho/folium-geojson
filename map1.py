import folium

map = folium.Map(location=[-1.1993409323259936, 36.838099528619956], zoom_start=6)

fgs = folium.FeatureGroup(name="Surface Type")

# fgs.add_child(folium.GeoJson('Road.json', name="geojson",
#                              style_function=lambda x: {
#                                  'color': 'red' if x['properties']['CWSurfType'] == 'Gravel' and 'Earth' and 'Track'
#                                  else 'green'}))

fgc = folium.FeatureGroup(name="Surface Condition")

# fgc.add_child(folium.GeoJson('Road.json', name="geojson",
#                              style_function=lambda x: {
#                                  'color': 'green' if x['properties']['CWSurfCond'] == 'Good'
#                                  else 'orange' if x['properties']['CWSurfCond'] == 'Fair' else 'red'}))

map.add_child(fgs)
map.add_child(fgc)
map.add_child(folium.LayerControl())
map.save('Map1.html')

