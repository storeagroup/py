import requests

API_KEY = "service.1f98235496c2471da6a8997d0b474c2c"

search_url = "https://api.neshan.org/v1/search"

params = {
  "term": "کافی شاپ",
  "lat": 34.6401, 
  "lng": 50.8782,
  "limit": 50, 
  "api_key": API_KEY  
}

results = requests.get(search_url, params=params).json()

cafes = results.get("items") or []

for cafe in cafes:
  name = cafe.get("title")  
  address = cafe.get("address")
  
  print(name, address)


