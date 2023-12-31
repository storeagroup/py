# import requests

# api_key = "key"

# search_url = "https://api.neshan.org/v2/search?api_key="+api_key+"&type=cafe&point=34.6318,50.8746&radius=5000"

# results = requests.get(search_url).json()["results"] 

# cafes = results

# for cafe in cafes:
#   name = cafe["name"]
#   address = cafe["address"]
  
#   print(name)
#   print(address)
#   print("---------------")


# import requests

# api_key = "web.7f2b2baccc2043578d84ff6664725b77"

# test_url = "https://api.neshan.org/v2/reverse?api_key="+api_key+"&point=35.6961,51.4231"

# response = requests.get(test_url)

# if response.status_code == 200:
#   print("API Key is valid")
# else:
#   print("API Key is NOT valid - Error:"+ str(response.status_code))



# import requests

# api_key = "service.1f98235496c2471da6a8997d0b474c2c"
# search_term = "cofeshp" 
# lat = 35.6984
# lng = 51.3390

# url = f"https://api.neshan.org/v1/search?term={search_term}&lat={lat}&lng={lng}"  

# headers = {"Api-Key": api_key}

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     search_results = response.json()
# else:
#     print("Error:", response.status_code)
#     search_results = None


# html = """<html>
# <head>
# <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
# </head> 
# <body class="bg-gray-100">
# <!-- HTML content --> 
# </body>
# </html>"""

# if search_results:
#     # Add search results to HTML
#     html_content = <!-- Generate HTML using Tailwind classes -->   
#     html = html.replace("<!-- HTML content -->", html_content)

# print(html)



# import requests

# api_key = "service.1f98235496c2471da6a8997d0b474c2c"  

# params = {
#   "term": "کافی شاپ",
#   "bbox": [50.5, 34.5, 51.5, 35.5],  
#   "api_key": api_key
# }

# search_url = "https://api.neshan.org/v1/search"
# results = requests.get(search_url, params=params).json()
# for item in results:
#    print(item)


# import requests

# API_KEY = "service.1f98235496c2471da6a8997d0b474c2c"

# search_url = "https://api.neshan.org/v1/search"

# params = {
#   "term": "کافی شاپ",
#   "lat": 34.6401, 
#   "lng": 50.8782,
#   "limit": 50, 
#   "api_key": API_KEY  
# }

# results = requests.get(search_url, params=params).json()

# cafes = results.get("items") or []

# for cafe in cafes:
#   name = cafe.get("title")  
#   address = cafe.get("address")
  
#   print(name, address)


import requests
from fpdf import FPDF

api_key = "service.1f98235496c2471da6a8997d0b474c2c"
search_term = "cafe"
lat = 35.6984
lng = 51.3390

url = f"https://api.neshan.org/v1/search?term={search_term}&lat={lat}&lng={lng}"

headers = {
    "Api-Key": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print("Error:", response.status_code) 

response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()
    
    pdf = FPDF(encoding='UTF-8')
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    
    pdf.cell(200, 10, txt = "List of Cafes",  
         ln = 1, align = 'C') 

    pdf.cell(100, 10, txt = "Name", border = 1)
    pdf.cell(100, 10, txt = "Address", border = 1)
    pdf.ln(10)
    
    for cafe in result["items"]:
        name = cafe["title"]
        address = cafe["address"]
        
        pdf.cell(100, 10, txt = name, border = 1)
        pdf.cell(100, 10, txt = address, border = 1)
        pdf.ln(10)
        
    pdf.output("cafes.pdf") 
    
    print("PDF saved successfully")
    
else:
    print("Error:", response.status_code)