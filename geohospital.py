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

def get_html_bpjs(url):  # post to get response from bpks
    address = {'jnsppk': "R", 'kdprop': "13", 'nmppk': ""}
    print(f"Sending POST request to {url} with payload: {address}")
    try:
        response = requests.post(url, json=address, headers=headers, timeout=10, )
        print(f"Received response with status code: {response.status_code}")
        response_data = response.json()
        print(f"Response JSON: {response_data}")
        return response_data
    except Exception as e:
        print(f"An error occurred: {e}")
        # print(response.status_code)
        return []

def get_lat_long(): # get lat long from address
    origin = get_html_bpjs('https://faskes.bpjs-kesehatan.go.id/aplicares/Peta/getData')
    print(f"Received origin data: {origin}")
    return origin
        
def get_ip(): # get keys and value from piAPI
    print("Fetching IP information from API...")
    api = get_html_json('https://ipapi.co/json/')
    print(f"API response: {api}")
    new = {
        'city': api['city'],
        'latitude': api['latitude'],
        'longitude': api['longitude']}
    print(f"Parsed IP information: {new}")
    return new

def distance(): # calculate distance between two points
    print("Fetching nearest hospital locations...")
    nearest_hospital = get_lat_long() # [{'nmppk': 'anu', 'lat':123, 'long':234}, {}, {}]
    print(f"Received nearest hospital data: {nearest_hospital}")
    print("Fetching current location...")
    current_location = get_ip()
    print(f"Received current location data: {current_location}")
    current_lat_long = (current_location['latitude'], current_location['longitude'])
    print(f"Current location coordinates: {current_lat_long}")

    for hospital in nearest_hospital:
        nearest_lat_long = (hospital['latitude'], hospital['longitude'])
        res =  geodesic(current_lat_long, nearest_lat_long).km
        print(f"Calculating distance from current location to {hospital['nmppk']}: {res} km")
        hospital['distance'] = res
        
    print("Finding the nearest hospital...")
    x = min(nearest_hospital, key=lambda x:x['distance'])
    print(f"Nearest hospital is {x['nmppk']} with distance of {x['distance']} km")
    return x

if __name__ == "__main__":
    # distance()
    # get_html_bpjs('https://faskes.bpjs-kesehatan.go.id/aplicares/Peta/getData')
    print(get_ip())