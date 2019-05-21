import requests
import json

# API constants for Yelp
api_host = 'https://api.yelp.com'
search_path = '/v3/businesses/search'

api_dir = '../../API_key_tacos-n-transit.txt'
#'../API_key_tacos-n-transit.txt'

#Open authentication key file
with open(api_dir) as file:
    data = file.read().splitlines()

#with read() adds new character line at the end. This allows no new character
api_key = data[0]

#To pass authentication key
headers = {'Authorization': "Bearer " + api_key}

#Parameters we are using to search. Maximum amount of restaurants returned is 50
url_params = {'latitude':32.8092908,'longitude':-117.1338192, 'radius':40000, \
              'term':'mexican', 'limit':50}

#url_params = {'latitude':32.8092908,'longitude':-117.1338192, \
#              'radius':40000, 'term':'mexican', 'limit':50, \
#              'sort_by':'distance,'open_now':True}

search = api_host + search_path

#Performing API get
response = requests.get(search,params=url_params,headers=headers)

#Passing list of businesses retrieved from yelp
businesses = response.json()['businesses']

