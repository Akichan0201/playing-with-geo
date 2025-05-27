import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from geohospital import get_lat_long, distance, get_ip


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Hello</h1>"

@app.get("/me")
async def get_api():
    return get_ip()

@app.get("/hospital")
async def hospital():
    return get_lat_long()

@app.get("/hospital/distance")
async def get_distance():
    return distance()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)


