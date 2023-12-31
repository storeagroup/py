# service.1f98235496c2471da6a8997d0b474c2c
import requests
API_KEY = "service.1f98235496c2471da6a8997d0b474c2c" 

api_url = "https://api.neshan.org/v1/search"

params = {
  "term": "coffee",
  "lat": 35.6998,
  "lng": 51.3380, 
  "apikey": API_KEY
}

headers = {
  "Api-Key": API_KEY
}

response = requests.get(api_url, params=params, headers=headers)
results = response.json()

print(f"Number of results found: {results['count']}")

for item in results["items"]:
  print(item["title"])
  print(item["address"])
  print("-"*30)

  html_content = """
<html>
<head>
<title>جستجو</title>  
</head>

<body>

<h1>نتایج جستجو</h1>

<ul>
"""

for item in results["items"]:
  title = item["title"]
  address = item["address"]
  
  html_content += f"<li>{title} <br> {address}</li>"

html_content += """
</ul>

</body>
</html>
"""

# ذخیره متن HTML در فایل

# with open("results.html","w") as f:
#   f.write(html_content)

with open("results.html","w", encoding="utf-8") as f:
  f.write(html_content) 
print("Results saved in results.html")