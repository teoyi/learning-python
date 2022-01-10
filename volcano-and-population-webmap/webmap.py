import folium
import pandas as pd
import os

# print(os.getcwd())

### Reading volcano address txt
# Change directory to one containing relevant .txt files
os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/volcanoes')
v_data = pd.read_csv("Volcanoes.txt")

### Seperating data to their statuses
vc = v_data[v_data['STATUS'].str.match('Varve Count')]
his = v_data[v_data['STATUS'].str.match('Historical')]
tep = v_data[v_data['STATUS'].str.match('Tephrochronology')]
pf = v_data[v_data['STATUS'].str.match('Pleistocene-Fumarolic')]
den = v_data[v_data['STATUS'].str.match('Dendrochronology')]
hol = v_data[v_data['STATUS'].str.match('Holocene')]
rc = v_data[v_data['STATUS'].str.match('Radiocarbon')]
ant = v_data[v_data['STATUS'].str.match('Anthropology')]

### Creating a color list to be assigned later
colorlst = ['red', 'blue', 'green', 'purple', 'orange', 'cadetblue','pink', 'black']

### Making webmap in html
# Change directory to one where the .html is to be saved
os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/mapping')
min_lon, max_lon = -200, 200
min_lat, max_lat = -90, 90
f = folium.Figure(width=1000, height=500)
map = folium.Map(location = [44.104014,-121.292043],
                 zoom_start = 5,
                 tiles = 'Stamen Toner',
                 max_bounds = True,
                 min_lat=min_lat,
                 max_lat=max_lat,
                 min_lon=min_lon,
                 max_lon=max_lon)

### Defining function with arguments that are respective of the statuses
def addstatus(data, color):
    data
    geolat = list(data['LAT'])
    geolon = list(data['LON'])
    name = list(data['NAME'])
    status = list(data['STATUS'])
    elev = list(data['ELEV'])
    type = list(data['TYPE'])

    feature_group = folium.FeatureGroup('Status: ' + data['STATUS'].values[0])

    for lat,lon,name,status,elev,type in zip(geolat,geolon,name,status,elev,type):

        html = f'''<b>{name}</b> <br>
        <br>
         Status: {status} <br>
         Type: {type} <br>
         Elevation: {elev} m<br>
         Latitude: {lat} <br>
         Longitude: {lon}'''

        iframe = folium.IFrame(html,
                               width = 260,
                               height = 150)

        popup = folium.Popup(iframe, max_width = 260)

        feature_group.add_child(folium.CircleMarker(location = [lat,lon],
        popup = popup, color = color,
        fill = True, fill_opacity = 0.7))
        map.add_child(feature_group)

### Adding population layer

def addpop():
    # Change directory to one that contains the .json file
    os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/population')
    feature_group = folium.FeatureGroup('World Population')
    feature_group.add_child(folium.GeoJson(data = open('world.json', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']
    ['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else
    'red' }))

    # Changing directory back to one containing map.html
    os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/mapping')
    map.add_child(feature_group)


addpop()
addstatus(vc, colorlst[0])
addstatus(his, colorlst[1])
addstatus(tep, colorlst[2])
addstatus(pf, colorlst[3])
addstatus(den, colorlst[4])
addstatus(hol, colorlst[5])
addstatus(rc, colorlst[6])
addstatus(ant, colorlst[7])


map.add_child(folium.LayerControl())

map.save("map.html")
