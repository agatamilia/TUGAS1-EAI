import requests

url = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/AZ/0"

headers = {
	"X-RapidAPI-Key": "aa9a42ef2amshbe9ea8ebc8369d9p1e5926jsn3ca9e409fa0a",
	"X-RapidAPI-Host": "restaurants-near-me-usa.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())