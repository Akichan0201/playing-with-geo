# Playing-with-Geo

A FastAPI project that finds the nearest hospital from your location using data from the Indonesian Ministry of Health API. It uses geolocation logic with Geopy and is deployed on Vercel.

## STAR Summary

**Situation:** Locating nearby hospitals efficiently is important, but existing sources often lack simple and location-aware APIs.

**Task:** Build an API that takes user coordinates and returns a list of the nearest hospitals using official data.

**Action:**  
- Retrieved hospital data using the Ministry of Health's open API  
- Calculated distances using Geopy based on latitude and longitude  
- Built an API with FastAPI to serve the closest hospital data  
- Deployed the application to Vercel with `vercel.json` for configuration

**Result:**  
An accessible and fast API that returns nearby hospital information based on geolocation. It is publicly available at [playing-with-geo.vercel.app](https://playing-with-geo.vercel.app)

## Features

- Connects to the Ministry of Health API to fetch hospital data
- Uses Geopy to calculate nearest hospitals by coordinates
- Serves a JSON response through FastAPI
- Deployed on Vercel at: [playing-with-geo.vercel.app](https://playing-with-geo.vercel.app)

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Akichan0201/nearest-hospital-api.git
cd nearest-hospital-api
```

### 2. Install dependencies
``` bash
pip install fastapi geopy uvicorn requests
```

### 3. Run the server locally
``` bash
uvicorn main:app --reload
```

### 4. Access the Endpoint
```bash
http://127.0.0.1:8000/nearest-hospital?lat=YOUR_LAT&lon=YOUR_LON
```

## Deployment
The API is deployed on Vercel and configured using vercel.json. You can try the live version here:
playing-with-geo.vercel.app

---
