import requests
import json

SUN_API_URL = "https://api.sunrisesunset.io/json?"
LOC_API_URL = "https://geocoding-api.open-meteo.com/v1/search"

def main():
    def_lat = 43.0722   #Madison, WI
    def_lon = -89.4008

    # lat = input("Enter Latitude: ")
    # lon = input("Enter Longitude: ")
    location = input("Enter City: ")

    if not location:
        location = "Madison"

    geo_payload = {'name': location, 'count':1, 'language':'en'}
    geo_url = f"{LOC_API_URL}"
    geo_r = requests.get(geo_url, params=geo_payload)
    geo_response = geo_r.json()
    # print(json.dumps(geo_r.json(), indent=4))
    lat = geo_response["results"][0]["latitude"]
    lon = geo_response["results"][0]["longitude"]

    if not lat:
        lat = def_lat
    if not lon:
        lon = def_lon

    payload = {'lat': lat, 'lng': lon}
    get_url = f"{SUN_API_URL}"
    r = requests.get(get_url, params=payload)
    # print(json.dumps(r.json(), indent=4))
    response = r.json()
    sunrise = response["results"]["sunrise"]
    sunset = response["results"]["sunset"]

    print(f"{sunrise}\n{sunset}\n")

if __name__ == "__main__":
    main()
