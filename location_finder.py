## Handling Location Using the Google Maps API
import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyCclbUYGNjrpIZ6Rgur6M0X8NN8-d6kqN4')

train_demographics = pd.read_csv('traindemographics.csv')
test_demographics = pd.read_csv('testdemographics.csv')
frames = [train_demographics,test_demographics]
demographics = pd.concat(frames,axis = 0)

latitude = demographics['latitude_gps']
longitude = demographics ['longitude_gps']

data = pd.concat((latitude,longitude),axis = 1)

data['location'] = gmaps.reverse_geocode((data.latitude_gps.values,data.longitude_gps.values))[0]['address_components'][2]['long_name']
