# Nearest Hospital Locator API

A FastAPI project that finds the nearest hospital from your location using data from the Indonesian Ministry of Health's API. It uses geolocation logic with Geopy and is deployed on Vercel.

## STAR Summary

**Situation:** Finding nearby hospitals quickly can be critical, but many sources do not offer location-based filtering in a simple API format.

**Task:** Build an API that returns the nearest hospitals from a given location by using official health data and geolocation tools.

**Action:**  
- Fetched hospital data using the official API from the Indonesian Ministry of Health  
- Calculated distance from user's coordinates to hospitals using Geopy  
- Built a FastAPI backend to serve the nearest results as an endpoint  
- Deployed the API to Vercel and configured it using `vercel.json`

**Result:**  
Created a working and deployable API that returns the nearest hospitals based on user-provided coordinates. This API is publicly available at [playing-with-geo.vercel.app](https://playing-with-geo.vercel.app)

## Features

- Retrieves hospital data from Kementerian Kesehatan API
- Calculates nearest hospitals using latitude and longitude
- Returns JSON data via FastAPI endpoint
- Deployed and live at: [playing-with-geo.vercel.app]

## How to Use

```bash
git clone https://github.com/Akichan0201/nearest-hospital-api.git
cd nearest-hospital-api
pip install -r requirements.txt
uvicorn main:app --reload
```
then access this:
http://127.0.0.1:8000/nearest-hospital?lat=YOUR_LAT&lon=YOUR_LON

---

Let me know if you want to add Swagger UI support, more filters (like hospital type), or a frontend to consume the API.
