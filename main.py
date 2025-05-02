from fastapi import FastAPI
from geohospital import get_lat_long, distance, get_ip


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello this is my API for finding nearest hospital",
            'me': 'if you want to get your location, please go to /me',
            'distance':'if you want to get distance, please go to /distance',
            'hospital': 'if you want to get nearest hospital, please go to /hospital'
            }

@app.get("/me")
async def get_api():
    return get_ip()

@app.get("/hospital")
async def hospital():
    return get_lat_long()

@app.get("/hospital/distance")
async def get_distance():
    return distance()