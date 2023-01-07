# Import the folium library, which provides functions for creating and manipulating interactive maps
import folium

# Initialize a Map object centered at the given latitude and longitude and with a starting zoom level of 6
map = folium.Map(location=[-1.1993409323259936, 36.838099528619956], zoom_start=6)

# Create a FeatureGroup object called 'Surface Type'
fgs = folium.FeatureGroup(name="Surface Type")

# Add a GeoJSON layer to the 'Surface Type' FeatureGroup with a style function that colors features red if their surface type is 'Gravel', 'Earth', or 'Track', and green otherwise
# fgs.add_child(folium.GeoJson('Road.json', name="geojson",
#                              style_function=lambda x: {
#                                  'color': 'red' if x['properties']['CWSurfType'] == 'Gravel' and 'Earth' and 'Track'
#                                  else 'green'}))

# Create a FeatureGroup object called 'Surface Condition'
fgc = folium.FeatureGroup(name="Surface Condition")

# Add a GeoJSON layer to the 'Surface Condition' FeatureGroup with a style function that colors features green if their surface condition is 'Good', orange if it is 'Fair', and red otherwise
# fgc.add_child(folium.GeoJson('Road.json', name="geojson",
#                              style_function=lambda x: {
#                                  'color': 'green' if x['properties']['CWSurfCond'] == 'Good'
#                                  else 'orange' if x['properties']['CWSurfCond'] == 'Fair' else 'red'}))

# Add the 'Surface Type' and 'Surface Condition' FeatureGroups to the map
map.add_child(fgs)
map.add_child(fgc)

# Add a layer control to the map, which allows the user to toggle the visibility of the 'Surface Type' and 'Surface Condition' layers
map.add_child(folium.LayerControl())

# Save the map to an HTML file called 'Map1.html'
map.save('Map1.html')

