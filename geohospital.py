import requests


from fastapi import FastAPI
from geopy.distance import geodesic


app = FastAPI()

headers = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36'
} # user agent added for avoiding redlimit

def get_html_json(url): # get dict from url piAPI
    response = requests.get(url, headers=headers)
    return response.json()

def get_html_bpjs(url): #post to get response from bpks
    address = {'jnsppk': "R", 'kdprop': "13", 'nmppk': ""}
    response = requests.post(url, json=address)
    return response.json()

def get_lat_long(): # get lat long from address
    origin = get_html_bpjs('https://faskes.bpjs-kesehatan.go.id/aplicares/Peta/getData')
    return origin
        
def get_ip(): # get keys and value from piAPI
    api = get_html_json('https://ipapi.co/json/')
    new = {
        'city' : api['city'],
        'latitude' : api['latitude'],
        'longitude' : api['longitude']}
    return new

def distance_min(): # calculate distance between two points
    nearest_hospital = get_lat_long() # [{'nmppk': 'anu', 'lat':123, 'long':234}, {}, {}]
    current_location = get_ip()
    current_lat_long = (current_location['latitude'], current_location['longitude'])

    for hospital in nearest_hospital:
        nearest_lat_long = (hospital['latitude'], hospital['longitude'])
        res =  geodesic(current_lat_long, nearest_lat_long).km
        hospital['distance'] = res
        
    x = min(nearest_hospital, key=lambda x:x['distance'])
    print(x)

def distance_sort(): # calculate distance between two points
    nearest_hospital = get_lat_long() # [{'nmppk': 'anu', 'lat':123, 'long':234}, {}, {}]
    current_location = get_ip()
    current_lat_long = (current_location['latitude'], current_location['longitude'])

    for hospital in nearest_hospital:
        nearest_lat_long = (hospital['latitude'], hospital['longitude'])
        res =  geodesic(current_lat_long, nearest_lat_long).km
        hospital['distance'] = res
        
    x = sorted(nearest_hospital, key=lambda x:x['distance'])
    print(x)
        
if __name__ == "__main__":
    # distance()
    get_html_bpjs('https://faskes.bpjs-kesehatan.go.id/aplicares/Peta/getData')